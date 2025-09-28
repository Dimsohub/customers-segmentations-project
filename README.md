# Customers Segmentation Project

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/customers-segmentations-project/blob/main/explore_data.ipynb)

---

## 📌 Project overview
This project shows how to combine **SQL queries** and **Python-based Exploratory Data Analysis (EDA)** on a real-world dataset.  
The data contains transactions from a UK-based online retail store and is a common benchmark for practice and demos.

The workflow starts from the original Excel file, converts it into CSV/SQLite, and then explores the data with SQL and Python.

**The project covers:**
- Database creation from raw Excel/CSV files  
- Exploratory Data Analysis (EDA)  
- Data visualization with **Plotly**  
- Demonstration in both **Google Colab** and **Jupyter Notebook**

---

## 🚀 Project workflow

1. **Database creation**  
   - The original Excel/CSV file is processed with `create_db.py` or `run_create_db.ipynb`.  
   - This generates a SQLite database file: `online_retail.db`.  
   - The database was uploaded to Google Drive to make it easy to access from Colab and other environments.

2. **Data access**  
   - The database file is downloaded automatically via [`gdown`](https://github.com/wkentaro/gdown) in the notebooks.  
   - It is saved to the `data/` folder as `data/online_retail.db`.  
   - The same download code works in **both Colab and local Jupyter** — no changes required.

3. **Exploration and analysis**  
   - Performed in `explore_data.ipynb`.  
   - Includes SQL-based checks and aggregations, standard EDA (missing values, duplicates, distributions), and interactive Plotly visualizations.

---

## 📂 Repository structure
    customers-segmentations-project/
    ├── data/                 # local folder where the database will be downloaded (contains .gitkeep)
    │   └── .gitkeep
    ├── create_db.py          # script to create database from CSV/Excel
    ├── run_create_db.ipynb   # optional notebook to build the DB interactively
    ├── explore_data.ipynb    # main EDA notebook (Colab & Jupyter friendly)
    ├── requirements.txt
    ├── .gitignore
    └── README.md

---

## 🔧 Setup & quick start

### Option 1 — Run in Google Colab (recommended)
1. Click the **Open in Colab** badge at the top of this README.  
2. If you want to use your own copy of the DB, replace the `FILE_ID` in the notebook with your Drive file id.  
3. The notebook will download the DB into `data/online_retail.db` and run the analysis cells.

### Option 2 — Run locally in Jupyter
1. Clone the repo:
    ```
    git clone https://github.com/yourusername/customers-segmentations-project.git
    cd customers-segmentations-project
    ``` 
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Start Jupyter:
    ```
    jupyter notebook
    ```
4. Open `explore_data.ipynb`. The notebook will download the database into `data/online_retail.db` using `gdown`.  
   Alternatively, you can recreate the DB locally by running:
    ```
    python create_db.py
    ```
---

## 🧩 Quickstart code example
Copy-paste this into a notebook cell to check the connection:

    import sqlite3
    import pandas as pd

    conn = sqlite3.connect("data/online_retail.db")
    df = pd.read_sql_query("SELECT * FROM online_retail LIMIT 5;", conn)
    df.head()

---

## 🛠 Requirements
- Python 3.9+  
- pandas  
- plotly  
- gdown  
- sqlite3 (Python stdlib)

Install everything with:

    pip install -r requirements.txt

---

## 📊 Example insights
The notebooks produce a set of business-oriented visuals and findings, for example:
- Distribution of order values  
- Number of unique products and top sellers by revenue  
- Customer segmentation by purchase frequency and value  
- Most common product pairs (basket analysis)  
- An interactive dashboard that brings the charts together

These steps reflect a practical analyst workflow: **load → inspect → aggregate → visualize → interpret**.

---

## 📑 Dataset
Source: UCI Machine Learning Repository — *[Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail)* dataset.  
The dataset contains transactions between **2010-12-01** and **2011-12-09** for a UK-based online retailer.

---
