import requests
from bs4 import BeautifulSoup
import unittest

class TestGitHubPagesSite(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://ryukijano.github.io/Qiskit_on_Qubit/"

    def test_homepage(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Qiskit on Qubit", response.text)

    def test_broken_links(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            url = link.get('href')
            if url and url.startswith('/'):
                url = self.base_url + url[1:]
            if url:
                link_response = requests.get(url)
                self.assertEqual(link_response.status_code, 200, f"Broken link: {url}")

    def test_missing_assets(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        assets = soup.find_all(['img', 'script', 'link'])
        for asset in assets:
            url = asset.get('src') or asset.get('href')
            if url and url.startswith('/'):
                url = self.base_url + url[1:]
            if url:
                asset_response = requests.get(url)
                self.assertEqual(asset_response.status_code, 200, f"Missing asset: {url}")

if __name__ == '__main__':
    unittest.main()
