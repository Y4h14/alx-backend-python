#!/usr/bin/env python3
from client import GithubOrgClient, get_json
import unittest
from unittest.mock import Mock, patch, MagicMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """a unit test class for githuborg client class"""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc",  {'login': "abc"})
    ])
    @patch('get_json')
    def test_org(self, org, resp, mock_func):
        mock_func.return_value = MagicMock(return_value=resp)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), resp)
        mock_func.assert_called_once_with(
            f"https://api.github.com/orgs/{org}:"
        )
