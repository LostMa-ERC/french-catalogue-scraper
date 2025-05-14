from rich.progress import (
    Progress,
    BarColumn,
    SpinnerColumn,
    TimeElapsedColumn,
    TextColumn,
    MofNCompleteColumn,
)
from rich.console import Console
import casanova

from am_scraper.models import Description
from am_scraper.scrape import scrape_page


def from_url_command(url: str) -> None:
    console = Console()
    with Progress(
        TextColumn("{task.description}"),
        SpinnerColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as p:
        _ = p.add_task("Scraping...")
        console.print(url)
        modelled_data = scrape_page(url=url)
        console.print(modelled_data)


def from_file_command(infile: str, column: str, outfile: str) -> None:
    console = Console()
    addendum = list(Description.__annotations__.keys())
    total = casanova.count(infile)
    with (
        open(infile) as f,
        open(outfile, "w") as of,
        Progress(
            TextColumn("{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            console=console,
        ) as p,
    ):
        t = p.add_task("Scraping", total=total)
        enricher = casanova.enricher(f, of, add=addendum)
        for row, url in enricher.cells(column=column, with_rows=True):
            console.rule("Current")
            console.print(url)
            modelled_data = scrape_page(url=url)
            console.clear()
            console.rule("Result")
            console.print(url)
            console.print(modelled_data)
            enricher.writerow(row, add=modelled_data.model_dump().values())
            p.advance(t)
