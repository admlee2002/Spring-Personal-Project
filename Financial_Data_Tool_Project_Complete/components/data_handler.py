import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data(file):
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def clean_data(df):
    df = df.dropna(axis=1, how='all')
    df = df.dropna(axis=0, thresh=int(0.5 * df.shape[1]))
    df = df.fillna(0)
    return df

def calculate_ratios(df):
    ratios = {}
    try:
        ratios['Current Ratio'] = df['Total Current Assets'].sum() / df['Total Current Liabilities'].sum()
        ratios['Debt-to-Equity'] = df['Total Liabilities'].sum() / df['Shareholder Equity'].sum()
        ratios['Net Profit Margin'] = df['Net Income'].sum() / df['Total Revenue'].sum()
    except Exception as e:
        st.warning(f"Could not calculate all ratios. Check column names: {e}")
    return ratios