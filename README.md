# Сustomers segmentation project

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Dimsohub/customers-segmentations-project/blob/main/scripts/explore_data.ipynb)

## 📌 Project Overview
This project demonstrates how to combine **SQL queries** and **Python-based EDA (Exploratory Data Analysis)** on a real dataset.  
The dataset contains transactions from a UK-based online retail store and is widely used for data analysis practice.  
The workflow starts from the original XLSX file, then converts it to CSV for SQLite, and finally explores the data with SQL and Python.

**Key goals:**
- Build a reproducible SQLite database from the raw dataset.
- Explore the data using SQL queries inside Python.
- Visualize business insights with interactive Plotly charts.
- Make the workflow Colab-friendly so it can be run without local setup.
  
## 🛠 Database Creation
1. The original dataset comes as an **Excel file** from the UCI Repository.  
2. Using the script `src/create_db.py`, we converted it into a **SQLite database (`online_retail.db`)** for easier querying.  
3. The database was then uploaded to **Google Drive**, so the Colab notebook can automatically download it.  
4. For local use, you can also generate the database yourself by running:
   ```bash
   python src/create_db.py
   
## 📂 Repository Structure

```text
customers-segmentations-project/
  data/                    # location for storing the database locally
  scripts/
    create_db.py           # script to create database from CSV
    explore_data.ipynb     # exploratory data analysis notebook
  README.md
  requirements.txt
  .gitignore
```

## 🔧 Setup & Usage

### Option 1: Run in Google Colab (recommended)
Just click the badge above ☝️.  
- The notebook automatically downloads the database from **Google Drive** (you only need to update the `FILE_ID` if you use your own copy).  
- No local setup required.

### Option 2: Run locally
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```
2. Download the XLSX file from [UCI Repository](https://archive.ics.uci.edu/dataset/352/online+retail).  
3. Convert it to CSV.
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Run `create_db.py` to generate `online_retail.db` locally.
7. Place `the online_retail.db` file into the data/ folder. 
8. Open `explore_data.ipynb` in Jupyter or Google Colab.
9. In the notebook, comment out the Google Drive download part and replace it with a local connection
```
import sqlite3
import pandas as pd
conn = sqlite3.connect("data/online_retail.db")
query = "SELECT * FROM online_retail LIMIT 5;"
df = pd.read_sql_query(query, conn)
df.head()
```

## 🔧 Requirements

Python 3.9+

pandas

plotly

sqlite3-binary

Install dependencies:
```
pip install -r requirements.txt
```
## 📊 Example Insights

Order Value Destribution.

Number of Unique Products.

Proportion of Customers by Number of Purchases.

Top Most Commonly Purchased Product Pairs.

Dashboard combining all graphs for better presentation.

These insights mimic a real-life business analyst workflow: load → query → visualize → interpret.

## 📑 Dataset

The dataset is provided by the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail?utm_source=chatgpt.com)
It contains all transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based online retailer.
