from datetime import datetime
from app.shared.lift_service import LiftService

from unittest import mock, TestCase
import os


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


@mock.patch('app.shared.lift_service.get', side_effect=_mocked_winter_lift)
class TestLiftService(TestCase):
    def setUp(self) -> None:
        # override pipenv
        os.environ['SEASON'] = 'Winter'
        os.environ['MAMMOTH_WINTER_LIFT_STATUS_URL'] = 'http://localhost:8001'

    def test_winter_lifts_with_updated_time(self, mock_get):
        lifts_service = LiftService()
        lifts = lifts_service.fetch_lifts()
        lift = next(filter(lambda l: l['name'] == 'Broadway Express 1', lifts))

        mock_get.assert_called_once_with('http://localhost:8001')

        self.assertEqual(lift['name'], 'Broadway Express 1')
        self.assertEqual(lift['status'], 'Expected')
        self.assertEqual(lift['kind'], 'Quad')
        last_updated = lift['last_updated']
        # can be off by 1 because of PST/PDT
        self.assertAlmostEqual(last_updated.hour, 20, delta=1)
        self.assertEqual(last_updated.minute, 20)
        self.assertEqual(lift['season'], 'Winter')

    def test_winter_lifts_without_updated_time(self, mock_get):
        lifts_service = LiftService()
        lifts = lifts_service.fetch_lifts()
        lift = next(filter(lambda l: l['name'] ==
                    'Discovery Express 11', lifts))
        utcnow = datetime.utcnow()

        mock_get.assert_called_once_with('http://localhost:8001')

        self.assertEqual(lift['name'], 'Discovery Express 11')
        last_updated = lift['last_updated']
        self.assertEqual([last_updated.hour, last_updated.minute], [
                         utcnow.hour, utcnow.minute])
