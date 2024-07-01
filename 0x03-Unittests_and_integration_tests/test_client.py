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
    @patch('utils.get_json')
    def test_org(self, org, resp, mock_func):
        mock_func.return_value = MagicMock(return_value=resp)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), resp)
        mock_func.assert_called_once_with(
            f"https://api.github.com/orgs/{org}:"
            )

    def test_public_repos_url(self):
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock:
            mock.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @patch('utils.get_json')
    def test_public_repos(self, get_josn_mock):
        test_payload = {
            'repos_url': "https://api.github.com/users/facebook/repos",
            'repos': [
                {
                    "id": 381489928,
                    "node_id": "MDEwOlJlcG9zaXRvcnkzODE0ODk5Mjg=",
                    "name": "akd",
                    "full_name": "facebook/akd",
                    "private": False,
                    "owner": {
                      "login": "facebook",
                      "id": 69631,
                      }
                      },
                {
                    "id": 381489928,
                    "node_id": "MDEwOlJlcG9zaXRvcnkzODE0ODk5Mjg=",
                    "name": "akd",
                    "full_name": "facebook/akd",
                    "private": False,
                    "owner": {
                      "login": "facebook",
                      "id": 69631,
                      }
                    }]}

        get_josn_mock.return_value = test_payload['repos']
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock:
            mock.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient('facebook').public_repos(),
                ["akd", "akd"])
            mock.assert_called_once()
        get_josn_mock.assert_called_once()
