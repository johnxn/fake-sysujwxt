#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fakesysujwxt
import unittest
import sys

username = None
password = None

class TestFakeSysujwxt(unittest.TestCase):
    """ Testing Fake Sysujwxt functions."""

    def setUp(self):
        self.year = "2012-2013"
        self.term = "1"
        self.sno = username
        self.passwd = password
        self.course_type = '30'
        self.campus = '1'
        self.cookie = fakesysujwxt.login(self.sno, self.passwd)[1]

    def test_login_success(self):
        success, result = fakesysujwxt.login(self.sno, self.passwd)
        self.assertTrue(success)

    def test_login_failed(self):
        success, result = fakesysujwxt.login(self.sno, "")
        self.assertFalse(success)

    def test_get_score(self):
        success, result = fakesysujwxt.get_score(self.cookie, self.sno, self.year, self.term)
        self.assertTrue(success)

    def test_get_timetable(self):
        success, result = fakesysujwxt.get_timetable(self.cookie, self.year, self.term)
        self.assertTrue(success)

    def test_get_available_courses(self):
        success, result = fakesysujwxt.get_available_courses(self.cookie, self.year, self.term, '30', '1')
        self.assertTrue(success)

    def test_get_course_result(self):
        success, result = fakesysujwxt.get_course_result(self.cookie, self.year, self.term)
        self.assertTrue(success)

    def test_get_course_result_by_type(self):
        success, result = fakesysujwxt.get_course_result_by_type(self.cookie, self.year, self.term, self.course_type)
        self.assertTrue(success)

    def test_get_tno(self):
        success, result = fakesysujwxt.get_tno(self.cookie)
        self.assertTrue(success)

    # TODO set tno and grade
    # def test_get_required_credit(self):
        # success, result = fakesysujwxt.get_required_credit(self.cookie, self.grade, self.tno)
        # self.assertTrue(success)

    def test_get_earned_credit(self):
        success, result = fakesysujwxt.get_earned_credit(self.cookie, self.sno, self.year, self.term)
        self.assertTrue(success)

    def test_get_gpa(self):
        success, result = fakesysujwxt.get_gpa(self.cookie, self.sno, self.year, self.term)
        self.assertTrue(success)

    def test_expired_queries(self):
        success, result = fakesysujwxt.get_score(self.cookie[::-1], self.sno, self.year, self.term)
        self.assertEqual(result, 'expired')
        success, result = fakesysujwxt.get_timetable(self.cookie[::-1], self.year, self.term)
        self.assertEqual(result, 'expired')
        success, result = fakesysujwxt.get_available_courses(self.cookie[::-1], self.year, self.term, '30', '1')
        self.assertEqual(result, 'expired')
        success, result = fakesysujwxt.get_course_result(self.cookie[::-1], self.year, self.term)
        self.assertEqual(result, 'expired')
        success, result = fakesysujwxt.get_earned_credit(self.cookie[::-1], self.sno, self.year, self.term)
        self.assertEqual(result, 'expired')
        success, result = fakesysujwxt.get_gpa(self.cookie[::-1], self.sno, self.year, self.term)
        self.assertEqual(result, 'expired')

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) != 3:
        print 'Run tests using "python test.py USERNAME PASSWORD"'
        exit(-1)
    username = sys.argv[1]
    password = sys.argv[2]
    sys.argv.pop()
    sys.argv.pop()
    unittest.main()
