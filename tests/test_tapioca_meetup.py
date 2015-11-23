# coding: utf-8

import unittest
import requests

from tapioca_meetup import Meetup
from tapioca_meetup.resource_mapping import RESOURCE_MAPPING


class TestTapiocaMeetup(unittest.TestCase):

    def setUp(self):
        self.wrapper = Meetup()

    def test_resource_docs_exist(self):
        """
        Test that all docs in resource mapping
        return a 200 HTTP code
        """
        for endpoint in RESOURCE_MAPPING.values():
            response = requests.get(endpoint['docs'])
            assert response.status_code == 200

    def test_resource_docs_return_valid_information(self):
        """
        Testing resource docs return valid information using
        the proxy of the resource URL

        """
        # FIXME: is there a reasonable way to check this?
        pass

if __name__ == '__main__':
    unittest.main()
