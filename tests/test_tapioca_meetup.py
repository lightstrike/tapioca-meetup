# coding: utf-8

import unittest

from tapioca_meetup import Meetup


class TestTapiocaMeetup(unittest.TestCase):

    def setUp(self):
        self.wrapper = Meetup()


if __name__ == '__main__':
    unittest.main()
