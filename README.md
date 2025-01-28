# RDF Generator
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/judaicalink/rdf_generator/graphs/commit-activity)

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/judaicalink/rdf_generator/blob/master/LICENSE)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![PyPI - Downloads](https://img.shields.io/pypi/dm/rdf-generator)

![PyPI - Version](https://img.shields.io/pypi/v/rdf-generator)

The `rdf_generator` library provides tools for generating RDF datasets from various data sources, including scraped websites, Excel sheets, CSV files, text files, PDFs, and relational databases (PostgreSQL, MySQL, etc.). It aims to simplify the process of building RDF datasets, enabling seamless integration into linked data workflows.

---

## Features

- **Modular Parsers**: Support for CSV, Excel, PDFs, relational databases (PostgreSQL, MySQL), and BEACON files.  
- **Web Scraping**: Extract structured data from websites.  
- **RDF Generation**: Build RDF graphs using `rdflib`, complete with namespaces and serialization options.  
- **Customizable Workflows**: Easily extend and integrate with your data pipelines.  
- **Serialization Formats**: Generate RDF in Turtle, RDF/XML, JSON-LD, and other formats.

---

## Installation

### 1. Install from PyPI (Standard Method)
```bash
pip install rdf_generator
```

### 2. Install Directly from GitHub (Alternative Method)
You can clone the repository and install the library manually if it's not on PyPI yet:

`git clone https://github.com/judaicalink/rdf_generator.git
cd rdf_generator
pip install .`

Or, install it directly from GitHub using:

`pip install git+https://github.com/judaicalink/rdf_generator.git`

## Requirements

* Python 3.7 or higher

* Libraries:

Install dependencies with:
`pip install -r requirements.txt`

* Core dependencies include:
  * rdflib
  * pandas
  * requests
  * beautifulsoup4
  * PyPDF2
  * mysql-connector-python
  * psycopg2

## Usage

The `rdf_generator` library is designed to provide parsers for multiple data sources and utilities to generate RDF datasets. Below are examples for various data sources.

1. Generate RDF from CSV Files
```python
from rdf_generator.parsers.csv_parser import CSVParser
from rdf_generator.rdf_builder import RDFBuilder

csv_parser = CSVParser("data/people.csv")
data = csv_parser.read_csv()

# Generate RDF
rdf_builder = RDFBuilder()
for row in data:
    rdf_builder.add_person(row['Name'], row['Email'])

# Serialize RDF
print(rdf_builder.serialize(format="turtle"))
```

2. Generate RDF from PostgreSQL

```python
from rdf_generator.parsers.sql_parser import PostgreSQLParser
from rdf_generator.rdf_builder import RDFBuilder

# Connect to the database
db_parser = PostgreSQLParser(
    host="localhost",
    database="testdb",
    user="your_username",
    password="your_password"
)

# Fetch data
query = "SELECT name, email FROM people;"
data = db_parser.fetch_data(query)

# Generate RDF
rdf_builder = RDFBuilder()
for row in data:
    rdf_builder.add_person(row['name'], row['email'])

# Serialize RDF
print(rdf_builder.serialize(format="turtle"))
```

3. Generate RDF from Websites (Web Scraping)
```python
from rdf_generator.parsers.web_scraper import WebScraper
from rdf_generator.rdf_builder import RDFBuilder

# Scrape the website
scraper = WebScraper("https://example.com")
data = scraper.extract_data("h1")  # Extract all H1 elements

# Generate RDF
rdf_builder = RDFBuilder()
for item in data:
    rdf_builder.graph.add((rdf_builder.ns[item], rdf_builder.ns.title, rdf_builder.ns[item]))

# Serialize RDF
print(rdf_builder.serialize(format="turtle"))
```
4. Generate RDF from Excel Files
```python
from rdf_generator.parsers.excel_parser import ExcelParser
from rdf_generator.rdf_builder import RDFBuilder

# Parse the Excel file
excel_parser = ExcelParser("data/people.xlsx")
data = excel_parser.read_sheet(sheet_name="People")

# Generate RDF
rdf_builder = RDFBuilder()
for row in data:
    rdf_builder.add_person(row['Name'], row['Email'])

# Serialize RDF
print(rdf_builder.serialize(format="turtle"))
```


## Supported Parsers

Parser	Description
CSV	Parses CSV files and extracts data as dictionaries.
Excel	Parses Excel (.xls/.xlsx) files and handles multiple sheets.
PDF	Extracts text and tables from PDF files.
SQL	Fetches data from relational databases like PostgreSQL and MySQL.
BEACON	Parses BEACON link dump files for RDF generation.
Web	Scrapes websites to extract structured data.

## Serialization Formats

The `rdf_generator library supports the following RDF serialization formats:

* **Turtle:** `rdf_builder.serialize(format="turtle")`
* **RDF/XML:** `rdf_builder.serialize(format="xml")`
* **JSON-LD:** `rdf_builder.serialize(format="json-ld")`

# Example Dataset Workflow

Here’s an example pipeline to process multiple data sources and generate a combined RDF dataset:

```python
from rdf_generator.parsers.csv_parser import CSVParser
from rdf_generator.parsers.web_scraper import WebScraper
from rdf_generator.rdf_builder import RDFBuilder

rdf_builder = RDFBuilder()

# Parse CSV
csv_parser = CSVParser("data/people.csv")
for row in csv_parser.read_csv():
    rdf_builder.add_person(row['Name'], row['Email'])

# Scrape Website
web_scraper = WebScraper("https://example.com")
titles = web_scraper.extract_data("h1")
for title in titles:
    rdf_builder.graph.add((rdf_builder.ns[title], rdf_builder.ns.label, rdf_builder.ns[title]))

# Serialize RDF
with open("output.ttl", "w") as f:
    f.write(rdf_builder.serialize(format="turtle"))
```

# Development

## Clone the Repository
To contribute or use the library without installation:
`
git clone https://github.com/yourusername/rdf_generator.git
cd rdf_generator
`

## Install Dependencies
Install dependencies using:

`pip install -r requirements.txt`

## Run Tests
Run unit tests using:

`python -m unittest discover -s tests`

# License

This library is licensed under the MIT License. See the LICENSE file for details.

# Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.
Create a feature branch: `git checkout -b feature-name`.
Commit your changes: `git commit -m "Add feature name"`.
Push to the branch: `git push origin feature-name.
Submit a pull request.
