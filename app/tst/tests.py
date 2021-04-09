from .constants import TEST_GUILD_ID, TEST_URI, TEST_EMPTY_WIDGET_RESPONSE, TEST_POPULATED_WIDGET_RESPONSE, \
    TEST_USER_STATUS
from ..src.constants import DISCORD_WIDGET_URI
from ..src.main import app
from unittest import TestCase
from requests import codes

import responses


class DiscordUserDownDetectorTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    @responses.activate
    def test_guild_not_found(self):
        responses.add(responses.GET, DISCORD_WIDGET_URI.format(TEST_GUILD_ID), status=codes.not_found)
        self.assertEqual(self.client.get(TEST_URI).status_code, codes.not_found)

    @responses.activate
    def test_member_not_found(self):
        responses.add(responses.GET, DISCORD_WIDGET_URI.format(TEST_GUILD_ID),
                      json=TEST_EMPTY_WIDGET_RESPONSE, status=codes.ok)
        self.assertEqual(self.client.get(TEST_URI).status_code, codes.not_found)

    @responses.activate
    def test_member_found(self):
        responses.add(responses.GET, DISCORD_WIDGET_URI.format(TEST_GUILD_ID),
                      json=TEST_POPULATED_WIDGET_RESPONSE, status=codes.ok)
        response = self.client.get(TEST_URI)
        self.assertEqual(response.status_code, codes.ok)
        self.assertEqual(response.json, {'status': TEST_USER_STATUS})