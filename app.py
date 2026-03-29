import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Prime Trade Project", layout="wide")

st.title("📈 Prime Trade Analysis Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    st.subheader("📌 Dataset Info")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Column selection
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_cols) > 0:
        col1, col2 = st.columns(2)

        with col1:
            x_axis = st.selectbox("Select X-axis", numeric_cols)

        with col2:
            y_axis = st.selectbox("Select Y-axis", numeric_cols)

        # Plotting
        st.subheader("📉 Visualization")

        fig, ax = plt.subplots()

        plot_type = st.radio("Choose Plot Type", ["Line", "Scatter", "Histogram"])

        if plot_type == "Line":
            ax.plot(df[x_axis], df[y_axis])
        elif plot_type == "Scatter":
            ax.scatter(df[x_axis], df[y_axis])
        elif plot_type == "Histogram":
            ax.hist(df[x_axis], bins=20)

        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)

        st.pyplot(fig)

        # Correlation heatmap
        st.subheader("🔥 Correlation Heatmap")
        fig2, ax2 = plt.subplots()
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax2)
        st.pyplot(fig2)

    else:
        st.warning("No numeric columns found in dataset.")

else:
    st.info("Please upload a CSV file to get started.")
