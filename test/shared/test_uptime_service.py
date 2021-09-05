import datetime
from app.shared.uptime_service import UptimeService

from unittest import mock, TestCase
import os
import json


def _load_latest_updates(filename: str) -> list:
    with open(filename, 'r') as file:
        text = file.read()
        data = json.loads(text)

    return data


class TestUptimeService(TestCase):
    @mock.patch.dict(os.environ, {'SEASON': 'Summer'})
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

    @mock.patch.dict(os.environ, {'SEASON': 'Summer'})
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

        # TODO: This 100 isn't entirely true since the lifts close early
        self.assertAlmostEqual(uptime, 100, delta=5)

    @mock.patch.dict(os.environ, {'SEASON': 'Summer'})
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

        # TODO: Similarly not entirely true because the closing time was early
        self.assertAlmostEqual(uptime, 75, delta=5)
