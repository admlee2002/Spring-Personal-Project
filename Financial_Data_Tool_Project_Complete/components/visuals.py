import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def display_visuals(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    if not numeric_cols.any():
        st.warning("No numeric columns found for visualization.")
        return

    selected_col = st.selectbox("Select a numeric column for visualization", numeric_cols)
    
    if selected_col:
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, ax=ax)
        st.pyplot(fig)

        st.line_chart(df[selected_col])