import requests
from bs4 import BeautifulSoup, exceptions
import logging

from ccfr_scraper.table_parser import TableParser
from ccfr_scraper.models import Description

logger = logging.getLogger("CCFR Scraper")
logging.basicConfig(
    filename="scraping.log",
    filemode="w",
    encoding="utf-8",
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def scrape_page(url: str) -> Description:
    resp = requests.get(url)
    if resp.status_code != 200:
        raise requests.RequestException()
    soup = BeautifulSoup(resp.content, "html.parser")
    try:
        tp = TableParser(soup=soup)
    except exceptions.FeatureNotFound:
        logger.warning(f"Content wasn't found on page: {url}")
        return Description(**{})
    return tp.model()
