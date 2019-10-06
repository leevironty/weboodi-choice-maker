import requests
from bs4 import BeautifulSoup
import datetime
import datetimerange
import dateutil
import time
from typing import List

# TODO: add docstrings


class Option:
    """An options holds a list of time ranges associated with choosing that option."""
    def __init__(self, name: str, dates: List[datetimerange.DateTimeRange]):
        self.name = name
        self.dates = dates
        self.proposed = True

    @staticmethod
    def get_option_from_soup(option_soup):
        name = option_soup(recursive=False)[1].tbody.tr.td.contents[0].strip()
        parts = option_soup(recursive=False)[1].table.tbody.tr(recursive=False)[-1].table.tbody.select("td")
        event_list_parts = [Option.get_daterange_list_from_soup(part) for part in parts]
        event_list = []
        for part in event_list_parts:
            event_list += part
        return Option(name, event_list)

    @staticmethod
    def get_daterange_list_from_soup(part):
        texts = [i.strip().replace("\xa0", " ") for i in part.strings][:2]
        t1, t2 = texts[1].split(" ")[1].split("-")
        h1, min1 = t1.split(".")
        h2, min2 = t2.split(".")
        time_start = dateutil.relativedelta.relativedelta(hours=int(h1), minutes=int(min1))
        time_end = dateutil.relativedelta.relativedelta(hours=int(h2), minutes=int(min2))

        if "-" in texts[0]:
            start_str, end_str = texts[0].split("-")
            d1, m1 = start_str.split(".")[:2]  # TODO: Tässä oletetaan, että päivämäärät ovat aina muotoa 1.2.-3.3.19
            d2, m2, y = end_str.split(".")
            start = datetime.datetime(int("20" + y), int(m1), int(d1))
            end = datetime.datetime(int("20" + y), int(m2), int(d2))
            diff = (end - start).days
            n = int(diff / 7) + 1
            week = dateutil.relativedelta.relativedelta(days=7)
            date_range_list = []
            for i in range(n):
                d = start + i * week
                date_range_list.append(datetimerange.DateTimeRange(d + time_start, d + time_end))
        else:
            start_str = texts[0]
            d1, m1, y = start_str.split(".")
            d = datetime.datetime(int("20" + y), int(m1), int(d1))
            date_range_list = [datetimerange.DateTimeRange(d + time_start, d + time_end)]
        return date_range_list


class Category:
    """A category of options. Usually one option must be chosen from each category."""
    def __init__(self, name, options):
        self.name = name
        self.options = options
        self.selected = None

    @staticmethod
    def get_categories_from_html(html):
        soup = BeautifulSoup(html, "lxml")
        tables = soup.select("form[name=ilmotForm] > table")
        categories = [Category.get_category_from_table_soup(table) for table in tables]
        return categories

    @staticmethod
    def get_category_from_table_soup(table):
        category_type = table.select("tbody > tr > th > table > tbody > tr > th")[1].contents[0].strip()
        options_html = table(recursive=False)
        options = [Option.get_option_from_soup(opt) for opt in options_html if "Aika ja Paikka" not in opt.getText()]
        return Category(category_type, options)

    @property
    def proposed(self):
        return [opt for opt in self.options if opt.proposed]

    @property
    def is_ready(self):
        return self.selected is not None

    def lock_selection(self):
        assert(len(self.proposed) == 1)
        self.selected = self.proposed[0]


class Course:
    def __init__(self, course_code):
        """A course object

        Keyword arguments:
        course_code -- course code for this Course object to represent
        """
        self.course_code = course_code
        api_url = f"https://oodi.aalto.fi/a/api/public/opetushaku/hae?nimiTaiTunniste={course_code}"
        response = requests.get(api_url).json()
        choices = [c for c in response[0]["opetustapahtumat"] if (not c["tentti"] and time.time() < c["ilmPaatPvm"])]
        choices.sort(key=lambda x: x["ilmPaatPvm"])
        course_id = choices[0]["opetustapahtumaId"]
        self.name = choices[0]["opintokohteenNimi"]
        html = Course.get_course_html(course_id)
        self.categories = Category.get_categories_from_html(html)

    @staticmethod
    def get_course_html(course_id):
        url = f"https://oodi.aalto.fi/a/opettaptied.jsp?OpetTap={course_id}"
        html = requests.get(url).text  # TODO: aina ei voi onnistua, catchaa errorit
        return html

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




