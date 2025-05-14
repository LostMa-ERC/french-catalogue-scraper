from bs4 import BeautifulSoup, exceptions
import re

from am_scraper.models import Description


class TableParser:
    def __init__(self, soup: BeautifulSoup):
        content = soup.find("contenu")
        if content is None:
            raise exceptions.FeatureNotFound()
        self.did = content.find("div", class_="did-class")
        self.pclass = content.find("div", class_="p-class")
        self.scope = content.find("div", class_="scopecontent-class")

    def model(self) -> dict:
        d = {
            "cote": self.cote,
            "old_cote": self.old_cote,  # list
            "repository": self.repository,
            "title": self.title,
            "date": self.date,
            "language": self.language,
            "physdesc": self.physdesc,  # list
            "digitization": self.digitization,
            "content": self.content,
        }
        model = Description.model_validate(d)
        return model

    @classmethod
    def clean_cotes(cls, tag, header: str) -> str:
        # Remove Réserve button
        [x.extract() for x in tag.find_all("a")]
        # Remove Cote prefix
        s = tag.get_text(strip=True)
        pattern = rf"{header}[^\S\r\n]:"
        cote_regexp = re.compile(pattern)
        s = cote_regexp.sub(repl="", string=s)
        return s.strip()

    @classmethod
    def clean_nested_html(cls, tag) -> str:
        s = tag.get_text(strip=True, separator=" ")
        return re.sub(pattern=r"\s{1}([,;\.]\s{1})", repl=r"\1", string=s)

    @property
    def cote(self) -> str | None:
        tag = self.did.find("div", class_="did-unitid")
        if tag is not None:
            return self.clean_cotes(tag=tag, header="Cote")

    @property
    def old_cote(self) -> list:
        results = []
        tags = self.did.find_all("div", class_="did-unitid")
        if len(tags) > 1:
            for tag in tags:
                if "Ancienne cote" not in tag.text:
                    continue
                cote = self.clean_cotes(tag=tag, header="Ancienne cote")
                results.append(cote)
            return results

    @property
    def repository(self) -> str | None:
        tag = self.did.find("div", class_="did-repository")
        if tag is not None:
            return tag.get_text(strip=True, separator=" ")

    @property
    def title(self) -> str | None:
        tag = self.did.find("div", class_="did-label")
        if tag is not None:
            return self.clean_nested_html(tag=tag)

    @property
    def date(self) -> str | None:
        tag = self.did.find("div", class_="did-date")
        if tag is not None:
            return tag.get_text(strip=True, separator=" ")

    @property
    def language(self) -> str | None:
        tag = self.did.find("div", class_="divdid", string=re.compile(r"rédigé en"))
        if tag is not None:
            s = self.clean_nested_html(tag=tag)
            language_regexp = re.compile(r"(?<=rédigé en ).*")
            match = language_regexp.search(s)
            if match is not None:
                s = match[0]
                return s.removesuffix(".")

    @property
    def physdesc(self) -> list:
        pars = []
        tags = self.did.find_all("div", class_="divdid")
        for tag in tags:
            if tag.text.strip().startswith("Ce document est rédigé en"):
                continue
            content = self.clean_nested_html(tag)
            pars.append(content)
        return pars

    @property
    def digitization(self) -> str | None:
        if self.pclass:
            tag = self.pclass.find("a", attrs={"title": "Voir le document numérisé"})
            if tag is not None:
                return tag.attrs["href"]

    @property
    def content(self) -> str | None:
        if self.scope:
            tag = self.scope.find("div", class_="description-part")
            if tag is not None:
                return self.clean_nested_html(tag=tag)
