from weboodi.course import Course
import copy


class Period:
    """Represents a teaching and evaluation period. It contains courses to be selected for said period."""
    def __init__(self):
        self.courses = []
        self.reserved_time = []
        self.results = []

    def add_course_by_code(self, code):
        """Add course to period by course code"""
        self.courses.append(Course(code))

    def add_block_to_calendar(self):  # TODO: implement
        """Add some block of time to calendar that prevents other activities"""
        pass

    def get_course_codes(self):
        """Return a list of course codes correspondig to courses selected for the period"""
        return [c.course_code for c in self.courses]

    def is_code_in_period(self, code):
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

    def make_selections(self):
        for course in self.courses:
            course.remove_empty_categories()
        self.results = self.thin_options(self.categories, [] + self.reserved_time)

    @staticmethod
    def disable_blocked_options(cats, dates):
        for cat in cats:
            for opt in [opt for opt in cat.options if opt.proposed]:
                for opt_date in opt.dates:
                    for sel_date in dates:
                        if opt_date.is_intersection(sel_date):
                            opt.proposed = False

    @staticmethod
    def select_only_options(cats):
        for cat in cats:
            if len(cat.proposed) == 1 and not cat.is_ready:
                cat.lock_selection()

    def thin_options(self, cats, dates):
        self.disable_blocked_options(cats, dates)
        # self.select_only_options(cats)
        for cat in cats:
            if len(cat.proposed) == 1 and not cat.is_ready:
                cat.lock_selection()
                dates += cat.selected.dates
        if all([cat.is_ready for cat in cats]):
            return [cats]
        # Ei helppoja ratkaisuja, otetaan siis joku ratkaisu ja jatketaan kunnes valmis
        results = []
        for i in range(len(cats)):
            if cats[i].is_ready:
                continue
            for j in range(len(cats[i].proposed)):
                cp_cats = copy.deepcopy(cats)
                cp_dates = dates[:]
                cat = cp_cats[i]
                s = cat.proposed[j]
                for opt in cat.proposed:
                    opt.proposed = False
                s.proposed = True
                cat.lock_selection()
                cp_dates += cat.selected.dates
                results += self.thin_options(cp_cats, cp_dates)
        return results
