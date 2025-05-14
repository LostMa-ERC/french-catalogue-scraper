import click
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

from ccfr_scraper.models import Description
from ccfr_scraper.scrape import scrape_page


@click.group
def cli():
    """Scrape the bibliographic, physical, and content descriptions from the notice of \
a document in the Catalogue collectif de France using the notice's URL."""
    pass


@cli.command("url")
@click.argument("url")
def from_url(url: str):
    """Scrape 1 URL."""
    console = Console()
    with Progress(
            TextColumn("{task.description}"),
            SpinnerColumn(),
            TimeElapsedColumn(),
            console=console,
        ) as p:
        t = p.add_task("Scraping...")
        console.print(url)
        modelled_data = scrape_page(url=url)
        console.print(modelled_data)


@cli.command("file")
@click.option(
    "-i", "--infile", required=True, help="Path to the CSV file with the notice URL."
)
@click.option(
    "-c", "--column", required=True, help="Column that contains the notice URL."
)
@click.option(
    "-o", "--outfile", required=True, help="Path to the output enriched CSV file."
)
def from_file(infile: str, column: str, outfile: str):
    """Scrape a set of URLs from a CSV file."""
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


if __name__ == "__main__":
    cli()
