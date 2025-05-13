from bs4 import BeautifulSoup, exceptions
import re

from ccfr_scraper.models import Description, Dimension


class TableParser:
    def __init__(self, soup: BeautifulSoup):
        content = soup.find(attrs={"itemtype": "http://schema.org/CreativeWork"})
        if content is None:
            raise exceptions.FeatureNotFound()
        self.soup = content

    def model(self) -> dict:
        dimensions = self.dimensions
        d = {
            "num": self.no,
            "cote": self.cote,
            "old_cote": self.old_cote,
            "date": self.date,
            "title": self.title,
            "language": self.language,
            "height": dimensions.height,
            "width": dimensions.width,
            "dimension_source": dimensions.source,
            "extent": self.extent,
            "support": self.support,
            "physical_characteristics": self.physical_characteristics,
            "decoration": self.decoration,
            "illustration": self.illustration,
            "marginalia": self.marginalia,
            "digitization": self.digitization,
            "content": self.content,
        }
        model = Description.model_validate(d)
        return model

    def find_data(self, header_text: str) -> list:
        results = []
        headers = self.soup.find_all("td", string=re.compile(header_text))
        for header in headers:
            data = header.find_next("td")
            if data is not None:
                results.append(data.text.strip())
        return results

    @property
    def no(self) -> str | None:
        header = self.soup.find("td", string=re.compile(r"N°"))
        if header:
            data = header.find_next("td")
            if data is not None:
                return data.text.strip()

    @property
    def cote(self) -> str | None:
        header = self.soup.find("td", string=re.compile(r"Cote"))
        if header:
            data = header.find_next("td")
            if data is not None:
                return data.text.strip()

    @property
    def content(self) -> str | None:
        header = self.soup.find("td", string=re.compile(r"contenu"))
        if header:
            data = header.find_next("td")
            if data is not None:
                return data.text.strip()

    @property
    def dimensions(self) -> Dimension:
        header = self.soup.find("td", string=re.compile(r"Dimensions"))
        if header:
            data = header.find_next("td")
            if data is not None:
                source = data.text.strip()
                return Dimension(source=source)
        return Dimension()

    @property
    def extent(self) -> str | None:
        header = self.soup.find("td", string=re.compile(r"Importance matérielle"))
        if header:
            data = header.find_next("td")
            if data is not None:
                return data.text.strip()

    @property
    def date(self) -> str | None:
        header = self.soup.find("td", string=re.compile(r"Date"))
        if header:
            data = header.find_next("td")
            if data is not None:
                return data.text.strip()

    @property
    def support(self) -> str | None:
        return self.find_data(header_text="Support")

    @property
    def old_cote(self) -> str | None:
        return self.find_data(header_text="Ancienne cote")

    @property
    def marginalia(self) -> str | None:
        return self.find_data(header_text="Marginalia")

    @property
    def illustration(self) -> str | None:
        return self.find_data(header_text="Illustration")

    @property
    def decoration(self) -> list:
        return self.find_data(header_text="Décoration")

    @property
    def physical_characteristics(self) -> list:
        return self.find_data(header_text="caractéristiques physiques")

    @property
    def title(self) -> str | None:
        return self.find_data(header_text="Titre")

    @property
    def language(self) -> str | None:
        return self.find_data(header_text="Langue")

    @property
    def digitization(self) -> str | None:
        return self.find_data(header_text="Numérisation")
