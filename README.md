# Mini AION Learning Prototype

## Overview

This is a small personal learning project inspired by the ingestion concepts discussed by AION.

The goal of this prototype was **not** to recreate AION, but to better understand how an ingestion pipeline could read Excel files, structure data, and compare different model versions.

## Current Features

- Read Excel files using Python
- Extract tracked outputs into a structured dictionary
- Compare two model versions
- Detect changed and unchanged values

## Technologies

- Python
- openpyxl

## Project Structure

```
parser.py
```

Reads an Excel file and converts it into a structured Python dictionary.

```
compare.py
```

Compares two model versions and highlights changed values.

## Purpose

This project was built as a personal learning exercise before starting a more complete ingestion prototype.

It helped me understand:

- Excel parsing
- Data structuring
- Version comparison
- Basic ingestion architecture

---

**Author:** Bruno Chaves Keller
