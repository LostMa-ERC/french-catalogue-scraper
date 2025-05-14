from typing import Annotated
from pydantic import BaseModel, Field, BeforeValidator, computed_field


def join_list(raw: list | None) -> str | None:
    if raw is not None and raw != "":
        return "|".join(raw)
    else:
        return None


class Description(BaseModel):
    cote: str | None = Field(default=None)
    old_cote: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    repository: str | None = Field(default=None)
    digitization: str | None = Field(default=None)
    date: str | None = Field(default=None)
    language: str | None = Field(default=None)
    title: str | None = Field(default=None)
    physdesc: Annotated[str | None, Field(default=None), BeforeValidator(join_list)]
    content: str | None = Field(default=None)


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
