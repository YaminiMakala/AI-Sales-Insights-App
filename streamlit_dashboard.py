import pandas as pd
from datetime import datetime
import streamlit as st

# Step 1: Load and Preprocess the Data
def preprocess_data(file_name="orders.csv"):
    df = pd.read_csv(file_name)
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    monthly_sales = df.groupby(df['OrderDate'].dt.to_period('M'))['TotalAmount'].sum()
    return df, monthly_sales

# Step 2: Build Streamlit Dashboard
def build_dashboard(df, monthly_sales):
    st.set_page_config(page_title="LLM Sales Dashboard", layout="centered")
    st.title("📊 Orders Dashboard")

    # Total Sales
    total_sales = df['TotalAmount'].sum()
    st.metric("💰 Total Sales", f"${total_sales:,.2f}")

    # Monthly Sales Chart
    st.subheader("📅 Monthly Sales Overview")
    monthly_sales_df = monthly_sales.reset_index()
    monthly_sales_df.columns = ["Month", "Total Sales"]
    st.line_chart(monthly_sales_df.set_index("Month"))

    # Filter Options
    st.subheader("📋 Orders Table")
    customer_filter = st.multiselect("Filter by Customer", df["CustomerName"].unique())
    status_filter = st.multiselect("Filter by Status", df["Status"].unique())

    filtered_df = df.copy()
    if customer_filter:
        filtered_df = filtered_df[filtered_df["CustomerName"].isin(customer_filter)]
    if status_filter:
        filtered_df = filtered_df[filtered_df["Status"].isin(status_filter)]

    st.dataframe(filtered_df)

if __name__ == "__main__":
    df, monthly_sales = preprocess_data()
    build_dashboard(df, monthly_sales)
