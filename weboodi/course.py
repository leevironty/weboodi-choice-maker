import requests
from bs4 import BeautifulSoup
import bs4
import datetime
from datetimerange import DateTimeRange
import dateutil
import time
import re
from typing import List
import weboodi.dates as dates

# TODO: add docstrings


class Option:
    """An options holds a list of time ranges associated with choosing that option."""

    def __init__(self, soup: bs4.Tag, category: 'Category'):
        name = soup(recursive=False)[1].tbody.tr.td.contents[0].strip()
        dates = self.get_dates_from_soup(soup)
        self.category = category
        self.name = name
        self.dates = dates
        self.proposed = True
        self.timestring = self.get_timestring(soup)

    def __str__(self):
        return f"Option {self.name}/{self.category.name}/{self.category.course.name}"


    @staticmethod
    def get_dates_from_soup(soup: bs4.Tag) -> List[DateTimeRange]:
        date_parts = soup(recursive=False)[1].table.tbody.tr(recursive=False)[-1].table.tbody.select("td")
        # is not none checks if there is no time given -> no event, so we skip it
        dateranges = [Option.get_daterange_list_from_soup(part) for part in date_parts if part.find("br") is not None]
        res = []
        for p in dateranges:
            res += p
        return res

    @staticmethod
    def get_daterange_list_from_soup(part: bs4.Tag) -> List[DateTimeRange]:
        texts = [i.strip().replace("\xa0", " ") for i in part.strings][:2]


        time_start, time_end = dates.get_deltas(texts[1].split(" ")[1])

        if "-" in texts[0]:
            start_str, end_str = texts[0].split("-")
            d1, m1 = start_str.split(".")[:2]  # TODO: Tässä oletetaan, että päivämäärät ovat aina muotoa 1.2.-3.3.19
            d2, m2, y = end_str.split(".")
            start = datetime.datetime(int("20" + y), int(m1), int(d1))
            end = datetime.datetime(int("20" + y), int(m2), int(d2))
            diff = (end - start).days
            n = diff // 7 + 1
            week = dateutil.relativedelta.relativedelta(days=7)
            date_range_list = []
            for i in range(n):
                d = start + i * week
                date_range_list.append(DateTimeRange(d + time_start, d + time_end))
        else:
            start_str = texts[0]
            d1, m1, y = start_str.split(".")
            d = datetime.datetime(int("20" + y), int(m1), int(d1))
            date_range_list = [DateTimeRange(d + time_start, d + time_end)]
        return date_range_list

    @staticmethod
    def get_timestring(soup: bs4.Tag) -> str:
        parts = soup(recursive=False)[1].table.tbody.tr(recursive=False)[-1].table.tbody.select("td")
        return ", ".join([Option.get_timestring_part(part) for part in parts])


    @staticmethod
    def get_timestring_part(part: bs4.Tag) -> str:
        texts = [i.strip().replace("\xa0", " ") for i in part.strings][:2]
        return " ".join(texts)


class Category:
    """A category of options. Usually one option must be chosen from each category."""

    def __init__(self, soup: bs4.Tag, course: 'Course'):
        category_type = soup.find_all(text=re.compile("Opettaja"))[0].parent.parent.th.text.strip()
        options_soup = soup.tbody(recursive=False)
        options = [Option(opt, self) for opt in options_soup if "Aika ja Paikka" not in opt.getText()]

        self.name = category_type
        self.options = options
        self.course = course
        self.selected = None
        self.important = True

    def __str__(self):
        return f"Category {self.name}/{self.course.name}, {'none selected' if self.selected is None else 'selected '+self.selected.name}"


    @property
    def proposed(self):
        return [opt for opt in self.options if opt.proposed]

    @property
    def is_ready(self):
        return self.selected is not None

    def lock_selection(self):
        self.selected = self.proposed[0]

    def reset(self):
        for opt in self.options:
            opt.proposed = True
        self.selected = None


class Course:
    def __init__(self, course_code: str, period: 'Period'):
        """A course object

        Keyword arguments:
        course_code -- course code for this Course object to represent
        """
        self.period = period
        self.course_code = course_code
        api_url = f"https://oodi.aalto.fi/a/api/public/opetushaku/hae?nimiTaiTunniste={course_code}"
        response = requests.get(api_url).json()
        choices = [c for c in response[0]["opetustapahtumat"] if (not c["tentti"] and time.time() < c["ilmPaatPvm"])]
        choices.sort(key=lambda x: x["ilmPaatPvm"])
        course_id = choices[0]["opetustapahtumaId"]
        self.name = choices[0]["opintokohteenNimi"]
        html = Course.get_course_html(course_id)
        #self.categories = Category.get_categories_from_html(html, self)

        category_soups = self.get_category_soups_from_html(html)
        self.categories = [Category(soup, self) for soup in category_soups]

    @staticmethod
    def get_course_html(course_id: str):
        url = f"https://oodi.aalto.fi/a/opettaptied.jsp?OpetTap={course_id}"
        html = requests.get(url).text  # TODO: aina ei voi onnistua, catchaa errorit
        return html

    @staticmethod
    def get_category_soups_from_html(html: str):
        soup = BeautifulSoup(html, "html5lib")  # Super important to be html5lib
        cats = soup.select(".kll")
        return cats

    @property
    def ready_categories(self):
        return [c for c in self.categories if c.selected]

    @property
    def is_ready(self):
        for c in self.categories:
            if not c.is_ready:
                return False
        return True

    def remove_empty_categories(self):
        for cat in self.categories:
            if len(cat.options) == 0:
                self.categories.remove(cat)

    def reset(self):
        for cat in self.categories:
            cat.reset()

