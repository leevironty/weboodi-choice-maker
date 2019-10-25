from weboodi.course import Course, Category, Option
from typing import List
from datetimerange import DateTimeRange
import weboodi.dates as dates


class Period:
    """Represents a teaching and evaluation period. It contains courses to be selected for said period."""
    def __init__(self):
        self.courses: List[Course] = []
        self.reserved_events: List[List[DateTimeRange]] = []
        self.results: List[Option] = []
        self.solutions: List[Solution] = []

    def add_course_by_code(self, code: str):
        """Add course to period by course code"""
        self.courses.append(Course(code, self))

    @property
    def reserved_time(self) -> List[DateTimeRange]:
        r = []
        for l in self.reserved_events:
            r += l
        return r

    def add_block_to_calendar(self, date_string: str):  # TODO: implement
        """Add some block of time to calendar that prevents other activities"""
        self.reserved_events.append(dates.get_event_list(date_string))

    def get_course_codes(self):
        """Return a list of course codes corresponding to courses selected for the period"""
        return [c.course_code for c in self.courses]

    def is_code_in_period(self, code: str):
        """Checks if a course with given code is already selected"""
        return code in self.get_course_codes()

    @property
    def categories(self):
        flat = []
        for cats in [c.categories for c in self.courses]:
            flat += cats
        return flat

    @property
    def selected(self):
        return [cat.selected for cat in self.categories if cat.is_ready]

    def clear_solutions(self):
        self.results = []
        self.solutions = []
        for course in self.courses:
            course.reset()

    def make_selections(self):
        for course in self.courses:
            course.remove_empty_categories()
        self.results = self.thin_options(self.categories, [] + self.reserved_time)
        self.solutions = [Solution(res, self) for res in self.results]

    @staticmethod
    def disable_blocked_options(cats, dates):
        for cat in cats:
            for opt in [opt for opt in cat.options if opt.proposed]:
                for opt_date in opt.dates:
                    for sel_date in dates:
                        if opt_date.is_intersection(sel_date):
                            opt.proposed = False

    @staticmethod
    def select_only_options(cats: List[Category]):
        """Goes through given categories and marks as selected options that don't have alternatives available."""
        for cat in cats:
            if len(cat.proposed) == 1 and not cat.is_ready:
                cat.lock_selection()

    def thin_options(self, cats: List[Category], dates: List[DateTimeRange]):
        """
        First this handles all easy choices, like only options and overlapping things. Then we recursively remove
        somethign until all choices are made.
        """
        self.disable_blocked_options(cats, dates)  # remove impossible options
        for cat in cats:  # select only options
            if len(cat.proposed) == 1 and not cat.is_ready:
                cat.lock_selection()
                dates += cat.selected.dates
        if all([cat.is_ready for cat in cats]):  # base solution: all categories are resolved
            return [[cat.selected for cat in cats]]

        # nothing to easily remove -> let's remove something
        results = []
        first_not_ready = None
        for i in range(len(cats)):  # We only need to consider the first non-ready category because of recursion
            if cats[i].is_ready:
                continue
            else:
                first_not_ready = i
                break

        for j in range(len(cats[first_not_ready].proposed)):  # Iterate through all possible options of chosen category
            cat = cats[first_not_ready]
            s = cat.proposed[j]
            to_reset = []  # Deep copies suck, so se just reset our objects
            for opt in cat.proposed:
                opt.proposed = False
                to_reset.append(opt)
            s.proposed = True
            cat.lock_selection()
            dates += cat.selected.dates

            results += self.thin_options(cats, dates)
            # reset dates and options
            for date in cat.selected.dates:
                dates.remove(date)
            for opt in to_reset:
                opt.proposed = True
            cat.selected = None
        return results


class Solution:
    def __init__(self, result: List[Option], period: Period):
        self.result = result
        self.period = period
        self.course_names = [course.name for course in period.courses]

    def __str__(self) -> str:
        s = "Selection\n\n"
        for course in self.course_names:
            s += f"{course}:\n"
            for res in self.result:
                if res.category.course.name == course:
                    timestring = res.timestring
                    # adds padding and newlines to make timestrings super nice
                    if ", " in timestring:
                        timestring = ("\n"+"\t"*self.tabs_to_timestring_start(res)).join(res.timestring.split(", "))
                    s += f"\t{res.name}  \t{timestring}\t\t({res.category.name})\n"
        return s

    @staticmethod
    def tabs_to_timestring_start(opt):
        return 2 + (len(opt.name) + 2)//4