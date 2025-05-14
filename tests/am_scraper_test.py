import unittest
from am_scraper.scrape import make_soup
from am_scraper.parser import TableParser


def make_description(url: str) -> TableParser:
    soup = make_soup(url=url)
    return TableParser(soup=soup)


CompleteNotice = make_description(
    url="https://archivesetmanuscrits.bnf.fr/ark:/12148/cc78503j"
)


class TestCompleteNotice(unittest.TestCase):
    tp = CompleteNotice

    def test_cote(self):
        self.assertIsNotNone(self.tp.cote)

    def test_old_cotes(self):
        self.assertEqual(len(self.tp.old_cote), 2)

    def test_repository(self):
        self.assertIsNotNone(self.tp.repository)

    def test_title(self):
        self.assertIsNotNone(self.tp.title)

    def test_language(self):
        self.assertIsNotNone(self.tp.language)

    def test_physdesc(self):
        first_description = self.tp.physdesc[0]
        self.assertGreater(len(first_description), 1_000)

    def test_digitization(self):
        self.assertIsNotNone(self.tp.digitization)

    def test_content(self):
        self.assertGreater(len(self.tp.content), 1_000)


if __name__ == "__main__":
    unittest.main()
