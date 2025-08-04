# 💰 Finance Manager

A Python script that parses your monthly bank CSV statements, categorizes transactions based on keywords, and uploads them to Google Sheets for easy tracking and analysis. 📊✨

---

## 🚀 Features

- Reads CSV files containing transaction data (date, name, amount)  
- Categorizes transactions like Amazon, Uber, subscriptions, food, transportation, and more! 🍕🚗📦  
- Uploads transactions directly to a Google Sheets document  
- Helps you visualize and manage your finances effortlessly  

---

## 🛠️ Technologies Used

- Python  
- CSV parsing (`csv` module)  
- Google Sheets API via `gspread`  
- Time delays for API rate limit handling (`time` module)  

---

## 📋 How It Works

1. Specify the month and CSV filename (e.g., `scotia_august.csv`).  
2. The script reads each transaction, applies keyword-based categorization rules, and standardizes transaction names.  
3. It uploads each categorized transaction to a dedicated worksheet in your Google Sheets spreadsheet.  

---

## ⚙️ Setup & Usage

### Prerequisites

- Python 3.x installed  
- `gspread` Python package (`pip install gspread`)  
- A Google Cloud service account JSON key file configured for Google Sheets API  
- Access to your Google Sheets document with proper sharing permissions to the service account  

### Running the Script

1. Place your CSV file (e.g., `scotia_august.csv`) in the same directory as the script.  
2. Update the `month` variable in the script to match your CSV month.  
3. Run the script:

```bash
python finance_manager.py
```
📁 File Format
- Your CSV should have rows formatted as:
- Date, Transaction Name, Amount

🔗 Links
- Google Sheets API docs: https://developers.google.com/sheets/api
- gspread library: https://gspread.readthedocs.io/en/latest/
