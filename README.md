# Сustomers segmentation project

This project analyzes the Online Retail dataset using SQL and Python.  
The workflow starts from the original XLSX file, then converts it to CSV for SQLite, and finally explores the data with Python.

## Project Workflow

1. **XLSX to CSV**  
   - The original dataset [`Online Retail.xlsx`](https://archive.ics.uci.edu/dataset/352/online+retail) is available on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail).  
   - Convert it to CSV because SQLite cannot import XLSX directly.

2. **CSV to SQLite Database**  
   - Using `create_db.py`, the CSV is cleaned and converted into a SQLite database `online_retail.db`.

3. **Exploratory Data Analysis**  
   - Analysis is performed in `explore_data.ipynb`.  
   - The notebook connects to `online_retail.db`, performs queries, counts product pairs, and visualizes data using Plotly and pandas.

## Usage

1. Download the XLSX file from [UCI Repository](https://archive.ics.uci.edu/dataset/352/online+retail).  
2. Convert it to CSV (optional: use the provided `create_db.py`).  
3. Run `create_db.py` to generate `online_retail.db` locally, or place your database in Google Drive.  
4. Open `explore_data.ipynb` in Jupyter or Google Colab.

### Accessing the Database in Colab

```python
from google.colab import drive
import sqlite3

# Mount Google Drive
drive.mount('/content/drive')

# Path to the database in your Drive
db_path = '/content/drive/MyDrive/OnlineRetailProject/online_retail.db'
conn = sqlite3.connect(db_path)
```
Users need either their own local copy of the database or access via Google Drive.

## Project Structure
customers-segmentations-project/
scripts/
create_db.py # script to create database from CSV
explore_data.ipynb # exploratory data analysis notebook
README.md
requirements.txt
.gitignore



