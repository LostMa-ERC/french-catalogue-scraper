import unittest
from ccfr_scraper.models import Dimension


class DimensionTest(unittest.TestCase):
    def test_x(self):
        text = "200 x 270 mm"
        d = Dimension(source=text)
        self.assertEqual(d.height, "200")
        self.assertEqual(d.width, "270")

    def test_special(self):
        text = "262 × 196 mm"
        d = Dimension(source=text)
        self.assertEqual(d.height, "262")
        self.assertEqual(d.width, "196")

    def test_quarto(self):
        text = "In-4o"
        d = Dimension(source=text)
        self.assertIsNone(d.height)
        self.assertIsNone(d.width)

    def test_sur(self):
        text = "300 sur 225 mm"
        d = Dimension(source=text)
        self.assertEqual(d.height, "300")
        self.assertEqual(d.width, "225")


if __name__ == "__main__":
    unittest.main()
