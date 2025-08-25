# Сustomers segmentations project

This project analyzes the Online Retail dataset using SQL and Python.  
The workflow starts from the original CSV file, then creates a SQLite database, and finally explores the data with Python.

## Project Workflow

1. **CSV to Database**  
   - The original dataset `Online Retail.csv` is stored in the `data/` folder.  
   - Using `create_db.py`, the CSV is cleaned and converted into a SQLite database `online_retail.db`.

2. **Exploratory Data Analysis**  
   - Analysis is performed in `explore_data.ipynb`.  
   - The notebook connects to `online_retail.db`, performs queries, counts product pairs, and visualizes data using Plotly and pandas.

## Project Structure

customers-segmentations-project/
│── data/
│ ├── Online Retail.csv # original CSV
│ └── online_retail.db # generated SQLite database
│── scripts/
│ ├── create_db.py # script to create database from CSV
│ ├── explore_data.ipynb # exploratory data analysis notebook
│── requirements.txt
│── README.md
│── .gitignore


## Database

- `online_retail.db` contains the cleaned Online Retail dataset.
- Table: `online_retail`
- Columns:
  - `invoiceno`
  - `stockcode`
  - `description`
  - `quantity`
  - `invoicedate`
  - `unitprice`
  - `customerid`
  - `country`

## Requirements

- Python 3.9+
- pandas
- plotly
- sqlite3-binary

Install dependencies:

```bash
pip install -r requirements.txt

Usage

Navigate to the scripts/ folder.

Run create_db.py to generate the database from CSV (if needed).

Open explore_data.ipynb to run analysis and visualizations.

