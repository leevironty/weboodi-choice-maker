import unittest
from weboodi.course import Course
from bs4 import BeautifulSoup as bs


class TestCourse(unittest.TestCase):
    def test_normal(self):
        course = Course("MS-C2111", None)
        self.assertEqual(course.name, "Stochastic Processes", "Name should be Stochastic Processes")
        self.assertEqual(len(course.categories), 3, "Should have 3 categories")
        self.assertFalse(course.is_ready, "Should not be ready")
