import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV
st.set_page_config(page_title="Airline Market Dashboard", layout="wide")
st.title("✈️ Airline Booking Market Demand Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("flights_data.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Flights")

airlines = st.sidebar.multiselect(
    "Select Airline(s)", options=df['airline'].unique(), default=df['airline'].unique()
)

statuses = st.sidebar.multiselect(
    "Select Status", options=df['status'].unique(), default=df['status'].unique()
)

df_filtered = df[
    (df['airline'].isin(airlines)) &
    (df['status'].isin(statuses))
]

# Show filtered table
st.subheader("📋 Filtered Flight Data")
st.dataframe(df_filtered, use_container_width=True)

# --- Charts Section ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Flights by Airline")
    airline_counts = df_filtered['airline'].value_counts().reset_index()
    airline_counts.columns = ['Airline', 'Flight Count']
    fig1 = px.bar(airline_counts, x='Airline', y='Flight Count', color='Airline')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🧮 Flight Status Distribution")
    status_counts = df_filtered['status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    fig2 = px.pie(status_counts, names='Status', values='Count')
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.caption("Made by Saral Pandey for PS Fin Solutions 🚀")
