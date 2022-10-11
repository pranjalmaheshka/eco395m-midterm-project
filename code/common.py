import requests
from bs4 import BeautifulSoup


def get_soup(url):

    """Takes a URL and returns a BeautifulSoup() instance representing the HTML of the page."""

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    return soup
