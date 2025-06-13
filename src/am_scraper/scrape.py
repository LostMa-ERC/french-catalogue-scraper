from urllib.request import Request, urlopen
from bs4 import BeautifulSoup, exceptions
import logging

from am_scraper.parser import TableParser
from am_scraper.models import Description

logger = logging.getLogger("AM Scraper")
logging.basicConfig(
    filename="scraping.log",
    filemode="w",
    encoding="utf-8",
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def make_soup(url: str) -> BeautifulSoup:
    # Request the page imitaing a browser (Mozilla Firefox)
    request = Request(url=url, headers={"User-Agent": "Mozilla/5.0"})
    content = urlopen(request).read()
    # Parse the HTML content with BeautifulSoup
    return BeautifulSoup(content, "html.parser")


def scrape_page(url: str) -> Description:
    # Request the page's HTML and parse it
    soup = make_soup(url)
    # Try to find the content's table on the page
    try:
        tp = TableParser(soup=soup)
    except exceptions.FeatureNotFound:
        message = f"Content wasn't found on page.\n\tURL: {url}"
        print(message)
        logger.warning(message)
        # If the table wasn't found, create an empty description
        return Description(**{})
    # Validate and model the parsed description metadata
    return tp.model()
