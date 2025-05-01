import streamlit as st
from components.data_handler import load_data, clean_data, calculate_ratios
from components.visuals import display_visuals

st.set_page_config(page_title="Financial Data Tool", layout="wide")
st.title("📊 Financial Data Analysis and Visualization Tool")

uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file:
    data = load_data(uploaded_file)
    if data is not None:
        st.subheader("Cleaned Data Preview")
        cleaned_data = clean_data(data)
        st.dataframe(cleaned_data)

        st.subheader("Financial Ratios")
        ratios = calculate_ratios(cleaned_data)
        if ratios:
            for key, value in ratios.items():
                st.metric(label=key, value=round(value, 2))

        st.subheader("Visualizations")
        display_visuals(cleaned_data)