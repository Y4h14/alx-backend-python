#!/usr/bin/env python3
"""defines a unittest class"""
from client import GithubOrgClient, get_json
import unittest
from unittest.mock import Mock, patch, MagicMock, PropertyMock
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

    def test_public_repos_url(self):
        with patch("GithubOrgClient.org",
                   new_callable=PropertyMock) as mock:
            mock.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                "https://api.github.com/users/google/repos"
            )
