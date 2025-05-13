from typing import Annotated
from pydantic import BaseModel, Field, BeforeValidator, computed_field


def join_list(raw: list) -> str | None:
    s = "|".join(raw)
    if s == "":
        return None
    else:
        return s


class Description(BaseModel):
    num: str | None = Field(default=None)
    cote: str | None = Field(default=None)
    old_cote: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    date: str | None = Field(default=None)
    title: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    language: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    height: str | None = Field(default=None)
    width: str | None = Field(default=None)
    dimension_source: str | None = Field(default=None)
    extent: str | None = Field(default=None)
    support: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    marginalia: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    illustration: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    decoration: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    physical_characteristics: Annotated[
        str | None, Field(default=None), BeforeValidator(join_list)
    ]
    digitization: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    content: str | None = Field(default=None)
    ecriture: str | None = Field(default=None, serialization_alias="script")
    reglure: str | None = Field(default=None, serialization_alias="ruling")
    codicology: str | None = Field(default=None)


class Dimension(BaseModel):
    source: str | None = Field(default=None)

    @computed_field
    @property
    def height(self) -> str | None:
        if self.source:
            s = self.source.split("×")
            if not len(s) == 2:
                s = self.source.split("x")
            if not len(s) == 2:
                s = self.source.split("sur")
            if len(s) == 2:
                return s[0].strip()

    @computed_field
    @property
    def width(self) -> str | None:
        if self.source:
            s = self.source.split("×")
            if not len(s) == 2:
                s = self.source.split("x")
            if not len(s) == 2:
                s = self.source.split("sur")
            if len(s) == 2:
                return s[1].replace("mm", "").strip()
