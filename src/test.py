"""
Unitests class
"""

import unittest
import requests
from controllers.operations import PlateOperations


class TestApi(unittest.TestCase):
    API_URL = 'http://0.0.0.0:5000/api'
    PLATES_URL = f'{API_URL}/plate'
    LEV_SEARCH = f'{API_URL}/search-plate'

    EMPTY_JSON_PARAMS = {}
    JSON_PARAMS = {'plate': 'KK-VB8932'}

    SEARCH_INVALID_PARAMS = {
        'key': 'GH-NJ8922',
        'levenshtein': 'A',
    }

    SEARCH_PARAMS = {
        'key': 'GH-NJ8922',
        'levenshtein': '2',
    }

    INVALID_PLATE = 'LG-AA20I0'
    VALID_PLATE = 'TY-RA2400'

    def teste_get_all_plates(self):
        request = requests.get(
            url=self.PLATES_URL,
        )

        self.assertEqual(request.status_code, 200)
        print('Success <teste_get_all_plates>')

    def teste_post_empty_json(self):
        request = requests.post(
            url=self.PLATES_URL,
            json=self.EMPTY_JSON_PARAMS,
        )

        self.assertEqual(request.status_code, 500)
        print('Success <teste_post_empty_json>')

    def teste_post_new_plate(self):
        request = requests.post(
            url=self.PLATES_URL,
            json=self.JSON_PARAMS,
        )

        self.assertEqual(request.status_code, 200)
        print('Success <teste_post_new_plate>')

    def teste_post_repeate_plate(self):
        request = requests.post(
            url=self.PLATES_URL,
            json=self.JSON_PARAMS
        )

        self.assertEqual(request.status_code, 500)
        print('Success <teste_post_repeate_plate>')

    def test_search_levenshtein_empty_params(self):
        request = requests.get(
            url=self.LEV_SEARCH,
        )

        self.assertEqual(request.status_code, 400)
        print('Success <test_search_levenshtein>')

    def test_search_levenshtein_invalid_params(self):
        request = requests.get(
            url=self.LEV_SEARCH,
            params=self.SEARCH_INVALID_PARAMS,
        )

        self.assertEqual(request.status_code, 400)
        print('Success <test_search_levenshtein_invalid_params>')

    def test_search_levenshtein_with_params(self):
        request = requests.get(
            url=self.LEV_SEARCH,
            params=self.SEARCH_PARAMS,
        )

        self.assertEqual(request.status_code, 200)
        print('Success <test_search_levenshtein_with_params>')

    def test_invalid_plate(self):
        test_plate = PlateOperations(self.INVALID_PLATE)
        self.assertTupleEqual(
            test_plate.check_plate_de(),
            (False, self.INVALID_PLATE)
        )
        print('Success <test_invalid_plate>')

    def test_valid_plate(self):
        test_plate = PlateOperations(self.VALID_PLATE)
        self.assertTupleEqual(
            test_plate.check_plate_de(),
            (True, self.VALID_PLATE)
        )
        print('Success <test_valid_plate>')


if __name__ == '__main__':
    tester = TestApi()
    tester.teste_get_all_plates()
    tester.teste_post_empty_json()
    tester.teste_post_new_plate()
    tester.teste_post_repeate_plate()
    tester.test_search_levenshtein_empty_params()
    tester.test_search_levenshtein_invalid_params()
    tester.test_search_levenshtein_with_params()
    tester.test_invalid_plate()
    tester.test_valid_plate()
