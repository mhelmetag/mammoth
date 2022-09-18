from app.shared.uptime_service import UptimeService

from unittest import TestCase
import os
import json


def _load_latest_updates(filename: str) -> list:
    with open(filename, 'r') as file:
        text = file.read()
        data = json.loads(text)

    return data


class TestUptimeService(TestCase):
    def setUp(self) -> None:
        # override pipenv
        os.environ['SEASON'] = 'Summer'

    def test_lift_not_open(self):
        seasonal_lifts = ['Stump Alley Express 2', 'Canyon Express 16',
                          'Discovery Express 11', 'Panorama Lower', 'Panorama Upper']
        day_of_week = 0
        latest_updates = _load_latest_updates(
            'test/shared/fixtures/lifts_with_no_downtime.json')

        uptime_service = UptimeService(
            seasonal_lifts, day_of_week, latest_updates)
        uptimes = uptime_service.calculate_uptimes()

        uptime = uptimes['Canyon Express 16']

        self.assertEqual(uptime, 0)

    def test_lifts_closed_early(self):
        seasonal_lifts = ['Stump Alley Express 2', 'Canyon Express 16',
                          'Discovery Express 11', 'Panorama Lower', 'Panorama Upper']
        day_of_week = 0
        latest_updates = _load_latest_updates(
            'test/shared/fixtures/lifts_with_no_downtime.json')

        uptime_service = UptimeService(
            seasonal_lifts, day_of_week, latest_updates)
        uptimes = uptime_service.calculate_uptimes()

        uptime = uptimes['Discovery Express 11']

        self.assertAlmostEqual(uptime, 94, delta=5)

    def test_lifts_with_downtime(self):
        seasonal_lifts = ['Stump Alley Express 2', 'Canyon Express 16',
                          'Discovery Express 11', 'Panorama Lower', 'Panorama Upper']
        day_of_week = 0
        latest_updates = _load_latest_updates(
            'test/shared/fixtures/lifts_with_downtime.json')

        uptime_service = UptimeService(
            seasonal_lifts, day_of_week, latest_updates)
        uptimes = uptime_service.calculate_uptimes()

        uptime = uptimes['Discovery Express 11']

        self.assertAlmostEqual(uptime, 75, delta=5)
