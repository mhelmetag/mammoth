from app.shared.lift_service import LiftService

from unittest import mock, TestCase
import os
from datetime import datetime
from dateutil.tz import gettz


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def _mocked_winter_lift(*args, **kwargs):
    with open('test/shared/fixtures/winter.html', 'r') as file:
        html = file.read()
        data = {
            'data': html,
            'success': True,
            'Message': None
        }

    return MockResponse(data, 200)


class TestLiftService(TestCase):
    @mock.patch.dict(os.environ, {'SEASON': 'Winter'})
    @mock.patch('app.shared.lift_service.get', side_effect=_mocked_winter_lift)
    def test_winter_lifts(self, mock_get):
        lifts_service = LiftService()
        lifts = lifts_service.fetch_lifts()
        lift = lifts[0]

        mock_get.assert_called_once_with('http://localhost:8001')

        self.assertEqual(lift['name'], 'Broadway Express 1')
        self.assertEqual(lift['status'], 'Expected')
        self.assertEqual(lift['kind'], 'Quad')
        self.assertEqual(lift['last_updated'], datetime(
            2021, 9, 5, 14, 20, tzinfo=gettz('America/Los_Angeles')))
        self.assertEqual(lift['season'], 'Winter')
