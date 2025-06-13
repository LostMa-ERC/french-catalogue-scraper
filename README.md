# French catalogue scrapers

HTML scrapers for gathering descriptive metadata from a document's notice in the Catalogue collectif de France or the Archives et Manuscrits in the Bibliothèque nationale de France's catalogue.

## Installation

1. Create a virtual Python environment of version 3.12 (or greater) and activate it.

2. Install the dependencies and script with `pip install git+https://github.com/LostMa-ERC/french-catalogue-scraper.git`

## Demos

The package has 2 scripts, one for each catalogue.

Explore what sort of metadata each scraper gets from its respective catalogue notice.

- [CCFR example](./demos/ccfr_output.csv)
- [Archives et Manuscrits example](./demos/am_output.csv)

## Catalogue collectif de France (`ccfr-scraper`)

You can run the CCFR scraper on a single URL, which will print the results in the terminal, or on a set of URLs from a CSV, which will write the results to a new CSV file.

### From 1 URL

Run the `ccfr-scraper url` subcommand with a URL (in quotation marks) as an argument.

```console
$ ccfr-scraper url "https://ccfr.bnf.fr/portailccfr/jsp/index_view_direct_anonymous.jsp?record=eadcgm:EADC:D29012180"
Scraping... ⠦ 0:00:02
```

### From CSV

Run the `ccfr-scraper file` subcommand with the following parameters:

- `-i` / `--infile` : path to the CSV file with the notices' URLs
- `-c` / `--column` : the column in the infile that has the URLs
- `-o` / `--outfile` : path to the file the program will produce / overwrite

```shell
ccfr-scraper file -i demos/ccfr_input.csv -c url -o demos/ccfr_output.csv
```

If the document's notice did not have a description that could be scraped, it will be reported in the log file, created at the path `scraping.log`. See the example below:

```log
2025-05-13 16:18:53,961 - CCFR Scraper - WARNING - Content wasn't found on page: https://ccfr.bnf.fr/portailccfr/ark:/16871/005FRCGMBPF-593506101-01a
```

## Archives et Manuscrits (`am-scraper`)

You can run the AM scraper on a single URL, which will print the results in the terminal, or on a set of URLs from a CSV, which will write the results to a new CSV file.

### From 1 URL

Run the `am-scraper url` subcommand with a URL (in quotation marks) as an argument.

```console
$ am-scraper url "https://archivesetmanuscrits.bnf.fr/ark:/12148/cc117974"
Scraping... ⠦ 0:00:01
```

### From CSV

Run the `am-scraper file` subcommand with the following parameters:

- `-i` / `--infile` : path to the CSV file with the notices' URLs
- `-c` / `--column` : the column in the infile that has the URLs
- `-o` / `--outfile` : path to the file the program will produce / overwrite

```shell
am-scraper file -i demos/am_input.csv -c url -o demos/am_output.csv
```
