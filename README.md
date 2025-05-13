# CCFR Scraper

HTML scraper for gathering descriptive metadata from a document's notice in the Catalogue collectif de France.

## Installation

1. Create a virtual Python environment of version 3.12 (or greater) and activate it.

2. Install the dependencies and script with `pip install .`

3. Test the installation.

```console
$ ccfr-scraper --help
Usage: ccfr-scraper [OPTIONS]

  Scrape the bibliographic, physical, and content descriptions from the notice
  of a document in the Catalogue collectif de France using the notice's URL.

Options:
  -i, --infile TEXT   Path to the CSV file with the notice URL.  [required]
  -c, --column TEXT   Column that contains the notice URL.  [required]
  -o, --outfile TEXT  Path to the output enriched CSV file.  [required]
  --help              Show this message and exit.
```

## Run

Run the `ccfr-scraper` command with the following parameters:

- `-i` / `--infile` : path to the CSV file with the notices' URLs
- `-c` / `--column` : the column in the infile that has the URLs
- `-o` / `--outfile` : path to the file the program will produce / overwrite

```shell
ccfr-scraper -i input.csv -c url -o output.csv
```

While the program processes the data file and its URLs, you can observe the results one by one in the terminal.


```console
────────────────────────── Result ───────────────────────────
https://ccfr.bnf.fr/portailccfr/jsp/index_view_direct_anonymous.jsp?record=eadcgm:EADC:D08A12666
Description(
    num='1142',
    cote='Ms O-53',
    old_cote='O.42',
    date='XIVe siècle',
    title='Adenet le Roi. Roman de Godefroy de Bouillon et Berte au grand pied',
    language='Français',
    height='218',
    width='152',
    dimension_source='218 × 152 mm',
    extent='140 feuillets',
    support='Parchemin',
    marginalia="Au f. 58, des visages sont dessinés à l'encre",
    illustration=None,
    decoration='Initiales nues rouges ou bleues',
    physical_characteristics='Texte manuscrit',
    digitization=None,
    content="f. 1 : « D... saiges et escientreus — ...a mains d'avoir et a plus de pechiés. Explicit le romant des caroniques despuis Godefroi de
Buillon. » L'écriture au recto du premier feuillet est presque entièrement effacée.f. 85 : Berte au grand pied. « A l'issue d'avril, un tans douz
et joli / Que herbelettes poignent et pré sont reverdi / ... Partent de Florimel mainte gent liemant/ ... De fresche herbe et de jons par tot
espessemant. » Il manque la fin."
)
────────────────────────── Current ──────────────────────────
https://ccfr.bnf.fr/portailccfr/jsp/index_view_direct_anonymous.jsp?record=eadcgm:EADC:b79374520
Scraping ━━╸━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  4/64 0:00:05

```

If the document's notice did not have a description that could be scraped, it will be reported in the log file, created at the path `scraping.log`. See the example below:

```log
2025-05-13 16:18:53,961 - CCFR Scraper - WARNING - Content wasn't found on page: https://ccfr.bnf.fr/portailccfr/ark:/16871/005FRCGMBPF-593506101-01a
```