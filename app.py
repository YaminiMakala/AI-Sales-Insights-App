import streamlit as st
import pandas as pd
import altair as alt
import datetime
from insights import get_sales_summary, load_llm
from db import get_all_sales, insert_sales_csv


st.set_page_config(page_title="LLM Sales Insights", layout="wide")

@st.cache_resource
def load_cached_llm():
    return load_llm()

llm = load_cached_llm()

st.title("📊 AskMySales: AI Sales Insights App")
st.markdown("Upload, filter, visualize, and query your sales with AI! 🤖")

# ===================== Upload CSV Section =====================
st.sidebar.header("📤 Upload Sales CSV")
uploaded_file = st.sidebar.file_uploader("Choose a file", type="csv")
if uploaded_file:
    inserted = insert_sales_csv(uploaded_file)
    st.sidebar.success(f"{inserted} new records added!")

# ===================== Sales Filters Section =====================
st.sidebar.header("🔍 Filter Sales")
sales = get_all_sales()
df = pd.DataFrame([vars(s) for s in sales])
df['date'] = pd.to_datetime(df['date'])

# Dropdown Filters
customers = df['customer_name'].unique()
products = df['product_name'].unique()
statuses = df['status'].unique()

start_date = st.sidebar.date_input("Start Date", value=df['date'].min())
end_date = st.sidebar.date_input("End Date", value=df['date'].max())
selected_customer = st.sidebar.multiselect("Customer", customers)
selected_product = st.sidebar.multiselect("Product", products)
selected_status = st.sidebar.multiselect("Status", statuses)

# Apply Filters
filtered_df = df[
    (df['date'] >= pd.to_datetime(start_date)) &
    (df['date'] <= pd.to_datetime(end_date))
]
if selected_customer:
    filtered_df = filtered_df[filtered_df['customer_name'].isin(selected_customer)]
if selected_product:
    filtered_df = filtered_df[filtered_df['product_name'].isin(selected_product)]
if selected_status:
    filtered_df = filtered_df[filtered_df['status'].isin(selected_status)]

# ===================== Display Filtered Sales =====================
st.subheader("💾 Sales Records")
st.dataframe(filtered_df[['date', 'customer_name', 'product_name', 'amount', 'status']])

# ===================== Bar Chart: Top Customers =====================
st.subheader("🏆 Top Customers by Revenue")
top_customers = (
    filtered_df.groupby('customer_name')['amount']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

chart = alt.Chart(top_customers).mark_bar().encode(
    x=alt.X('amount', title='Revenue'),
    y=alt.Y('customer_name', sort='-x', title='Customer'),
    color='customer_name'
).properties(height=400)

st.altair_chart(chart, use_container_width=True)

# ===================== LLM Q&A =====================
st.subheader("🤖 Ask a Sales Question")
question = st.text_input("e.g., What is the total revenue in April?")
if st.button("Get Insight"):
    if question:
        with st.spinner("AI is thinking..."):
            answer = get_sales_summary(question, llm)
        st.success(answer)

        # Option to download answer
        st.download_button("📄 Download Insight", answer, file_name="insight.txt")



