import streamlit as st

from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.analyzer import SalesAnalyzer


st.set_page_config(
    page_title="Sales Analytics Dashboard",
    layout="wide"
)

st.title("📊 Sales Analytics Dashboard")
st.caption(
    "A Python-based analytics dashboard for monitoring sales performance."
)


def load_and_process_data():
    loader = DataLoader("data/superstore_sales.csv")
    raw_df = loader.load_data()

    cleaner = DataCleaner(raw_df)
    clean_df = cleaner.clean_data()

    return clean_df


def main():
    try:
        df = load_and_process_data()
        analyzer = SalesAnalyzer(df)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

    # KPIs
    kpis = analyzer.get_kpis()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Sales", f"${float(kpis['total_sales']):,.2f}")
    col2.metric("Total Profit", f"${float(kpis['total_profit']):,.2f}")
    col3.metric("Total Orders", int(kpis["total_orders"]))
    col4.metric("Avg Discount", f"{float(kpis['avg_discount']) * 100:.0f}%")

    st.divider()

    # Charts
    st.subheader("Sales by Category")
    category_df = analyzer.sales_by_category()
    st.bar_chart(category_df.set_index("Category"))

    st.subheader("Sales by Region")
    region_df = analyzer.sales_by_region()
    st.bar_chart(region_df.set_index("Region"))

    st.divider()

    st.subheader("🏆 Top 10 Profitable Sub-Categories")

    top_subcat = analyzer.top_profitable_subcategories()
    st.bar_chart(top_subcat.set_index("Sub-Category"))

    st.divider()

    # Data table
    st.subheader("Raw Sales Data Preview")
    st.dataframe(df.head(50))


main()
