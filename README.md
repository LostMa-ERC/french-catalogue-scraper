# French catalogue scrapers

HTML scrapers for gathering descriptive metadata from a document's notice in the Catalogue collectif de France or the Archives et Manuscrits in the Bibliothèque nationale de France's catalogue.

## Installation

1. Create a virtual Python environment of version 3.12 (or greater) and activate it.

2. Install the dependencies and script with `pip install .`

3. Test the installation by viewing the CCFR scraper's `help` documentation.

```console
$ ccfr-scraper --help
Usage: ccfr-scraper [OPTIONS] COMMAND [ARGS]...

  Scrape the bibliographic, physical, and content descriptions from the notice
  of a document in the Catalogue collectif de France using the notice's URL.

Options:
  --help  Show this message and exit.

Commands:
  file  Scrape a set of URLs from a CSV file.
  url   Scrape 1 URL.
```

## Run

The package has 2 scripts, one for each catalogue.

### Catalogue collectif de France (`ccfr-scraper`)

You can run the CCFR scraper on a single URL, which will print the results in the terminal, or on a set of URLs from a CSV, which will write the results to a new CSV file.

#### From 1 URL

Run the `ccfr-scraper url` subcommand with a URL (in quotation marks) as an argument.

```console
$ ccfr-scraper url "https://ccfr.bnf.fr/portailccfr/jsp/index_view_direct_anonymous.jsp?record=eadcgm:EADC:D29012180"

Description(
    num='593',
    cote=None,
    old_cote=None,
    date='Début du XIVe siècle',
    title="Recueil|col. 1. Les prophéties de Merlin, traduites pour l'empereur Frédéric. « Ci commencent les profecies Merlin et ses euvres, et
les merveilles que il fist en la Grant Bretaigne et en maintes autres terres asés soutillement. Et pour ce s'en test atant li conte de ceste
matière. Et parole des profecies Merlin, qui sont translatées du latin en françois, que Fedelic a fait translater, por ce que li chevalier et li
autre gent laies les entendent miex et i puissent prendre aucune essample... »",
    language='français, latin|français, latin',
    height='370',
    width='247',
    dimension_source='370 × 247 mm',
    extent='538 feuillets, à 3 colonnes, au lieu de 544 constatés par un ancien foliotage (nos I-VcXLIII, plus un folio. V bis)',
    support='Parchemin',
    marginalia=None,
    illustration=None,
    decoration=None,
    physical_characteristics=None,
    digitization=None,
    content=None,
    ecriture=None,
    reglure=None,
    codicology=None
)
Scraping... ⠦ 0:00:02
```

#### From CSV

Run the `ccfr-scraper file` subcommand with the following parameters:

- `-i` / `--infile` : path to the CSV file with the notices' URLs
- `-c` / `--column` : the column in the infile that has the URLs
- `-o` / `--outfile` : path to the file the program will produce / overwrite

```shell
ccfr-scraper file -i input.csv -c url -o output.csv
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

### Archives et Manuscrits (`am-scraper`)

You can run the AM scraper on a single URL, which will print the results in the terminal, or on a set of URLs from a CSV, which will write the results to a new CSV file.

#### From 1 URL

Run the `am-scraper url` subcommand with a URL (in quotation marks) as an argument.

```console
$ am-scraper url "https://archivesetmanuscrits.bnf.fr/ark:/12148/cc117974"
```

#### From CSV

Run the `am-scraper file` subcommand with the following parameters:

- `-i` / `--infile` : path to the CSV file with the notices' URLs
- `-c` / `--column` : the column in the infile that has the URLs
- `-o` / `--outfile` : path to the file the program will produce / overwrite

```shell
am-scraper file -i input.csv -c url -o output.csv
```
