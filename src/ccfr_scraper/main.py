import click

from ccfr_scraper.commands import from_file_command, from_url_command


@click.group
def cli():
    """Scrape the bibliographic, physical, and content descriptions from the notice of \
a document in the Catalogue collectif de France using the notice's URL."""
    pass


@cli.command("url")
@click.argument("url")
def from_url(url: str):
    """Scrape 1 URL."""
    from_url_command(url=url)


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
    from_file_command(infile=infile, column=column, outfile=outfile)


if __name__ == "__main__":
    cli()
