#!/usr/bin/python3
""" unit test for file base.py """
import unittest



class TestBase(unittest.TestCase):
    """ unit testing class Base task 1. Base class """

    def test_aa_argumet_a(self):
        """ check empty argument send to function """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(None).id, 4)