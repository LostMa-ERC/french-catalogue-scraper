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
    request = Request(url=url, headers={"User-Agent": "Mozilla/5.0"})
    content = urlopen(request).read()
    return BeautifulSoup(content, "html.parser")


def scrape_page(url: str) -> Description:
    soup = make_soup(url)
    try:
        tp = TableParser(soup=soup)
    except exceptions.FeatureNotFound:
        message = f"Content wasn't found on page: {url}"
        print(message)
        logger.warning(message)
        return Description(**{})
    return tp.model()
