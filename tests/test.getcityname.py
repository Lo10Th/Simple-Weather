import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from getcityname import get_city_name


class TestGetCityName(unittest.TestCase):

    @patch('requests.get')
    def test_get_city_name_success(self, mock_get):
        mock_response = {
            "status_code": 200,
            "json.return_value": {
                "results": [
                    {
                        "address_components": [
                            {"long_name": "CityName1"},
                            {"long_name": "CityName2"},
                            {"long_name": "CityName3"},
                            {"long_name": "YourCityName"}
                        ]
                    }
                ]
            }
        }
        mock_get.return_value = unittest.mock.Mock(**mock_response) # type: ignore
        
        city_name = get_city_name(40.7128, -74.0060) 
        
        self.assertEqual(city_name, "YourCityName")

    @patch('requests.get')
    def test_get_city_name_api_failure(self, mock_get):
        mock_response = {
            "status_code": 500
        }
        mock_get.return_value = unittest.mock.Mock(**mock_response) # type: ignore
        
        with self.assertRaises(Exception):
            get_city_name(40.7128, -74.0060)
if __name__ == '__main__':
    unittest.main()
