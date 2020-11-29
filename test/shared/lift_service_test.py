from app.shared.lift_service import LiftService

from unittest import mock, TestCase
import os
import json


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mocked_winter_lift(*args, **kwargs):
    with open('test/shared/winter_lifts.json', 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)

        return MockResponse(data, 200)


class LiftServiceTest(TestCase):
    @mock.patch.dict(os.environ, {'SEASON': 'Winter'})
    @mock.patch('app.shared.lift_service.get', side_effect=mocked_winter_lift)
    def test_winter_lifts(self, mock_get):
        lifts_service = LiftService()
        lifts = lifts_service.fetch_lifts()
        lift = lifts[0]

        self.assertEqual(lift['name'], 'Broadway Express 1')
        self.assertEqual(lift['status'], 'Expected')
        self.assertEqual(lift['kind'], 'Quad')
        self.assertEqual(lift['season'], 'Winter')
