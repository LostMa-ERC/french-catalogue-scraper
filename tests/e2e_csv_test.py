import csv
from pathlib import Path
import unittest

from ccfr_scraper.commands import from_file_command as ccfr_csv
from am_scraper.commands import from_file_command as am_csv


CCFR_ROWS = [
    (
        "https://ccfr.bnf.fr/portailccfr/jsp/index_view_direct_anonymous.jsp?record=eadcgm:EADC:D15100069",
    ),
    (
        "https://ccfr.bnf.fr/portailccfr/jsp/index_view_direct_anonymous.jsp?record=eadcgm:EADC:D25010097",
    ),
]

AM_ROWS = [
    ("https://archivesetmanuscrits.bnf.fr/ark:/12148/cc11515n",),
    ("https://archivesetmanuscrits.bnf.fr/ark:/12148/cc115174",),
]


class AMTest(unittest.TestCase):
    infile = Path(__file__).parent.joinpath("infile.csv")
    outfile = Path(__file__).parent.joinpath("outfile.csv")

    def setUp(self):
        with open(self.infile, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["url"])
            writer.writerows(AM_ROWS)
        return super().setUp()

    def test_ccfr(self):
        am_csv(infile=self.infile, column="url", outfile=self.outfile)
        with open(self.outfile, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row["title"]
                self.assertIsNotNone(title)

    def tearDown(self):
        self.infile.unlink()
        self.outfile.unlink()
        return super().tearDown()


class CCFRTest(unittest.TestCase):
    infile = Path(__file__).parent.joinpath("infile.csv")
    outfile = Path(__file__).parent.joinpath("outfile.csv")

    def setUp(self):
        with open(self.infile, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["url"])
            writer.writerows(CCFR_ROWS)
        return super().setUp()

    def test_ccfr(self):
        ccfr_csv(infile=self.infile, column="url", outfile=self.outfile)
        with open(self.outfile, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                height = row["height"]
                self.assertIsNotNone(height)

    def tearDown(self):
        self.infile.unlink()
        self.outfile.unlink()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
