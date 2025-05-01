# Financial Data Analysis and Visualization Tool

This is a Python-based financial analysis app built using **Streamlit**, designed to help users upload, clean, analyze, and visualize financial data from CSV or Excel files.

## 🔧 Features
- File upload (.csv or .xlsx)
- Data cleaning (missing values handling)
- Financial ratio calculations:
  - Current Ratio
  - Debt-to-Equity Ratio
  - Net Profit Margin
- Histogram & line chart visualizations
- Simple UI built with Streamlit

## 📦 Tech Stack
- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- openpyxl

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial-data-tool.git
   cd financial-data-tool
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the app:
   ```bash
   streamlit run main.py
   ```

## 📁 Project Structure
```
Financial_Data_Tool_Project/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── components/
│   ├── data_handler.py
│   └── visuals.py
├── assets/
```

## 📄 License
This project is for educational use.