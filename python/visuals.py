import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("💳 Fraud Detection Analytics Dashboard")

# Connect to MotherDuck
con = duckdb.connect("md:")

# Load data
df = con.execute("SELECT * FROM fraud_risk_final").fetch_df()

# Sidebar filter
st.sidebar.header("Filters")
amount_category = st.sidebar.multiselect(
    "Select Amount Category",
    options=df["amount_category"].unique(),
    default=df["amount_category"].unique()
)

filtered_df = df[df["amount_category"].isin(amount_category)]

# ---- Fraud Distribution ----
st.subheader("Fraud vs Non-Fraud Distribution")

fraud_dist = (
    filtered_df.groupby("Class")
    .size()
    .reset_index(name="count")
)

fig1 = px.pie(
    fraud_dist,
    names="Class",
    values="count",
    title="Fraud Distribution (0 = Legit, 1 = Fraud)",
    color="Class",
    color_discrete_map={
        0: "green",
        1: "red"
    }

)

st.plotly_chart(fig1, use_container_width=True)

# ---- Risk Score Analysis ----
st.subheader("Fraud Rate by Risk Score")

risk_analysis = (
    filtered_df.groupby("total_risk_score")
    .agg(total=("Class", "count"),
         fraud=("Class", "sum"))
    .reset_index()
)

risk_analysis["fraud_rate"] = (
    100 * risk_analysis["fraud"] / risk_analysis["total"]
)

fig2 = px.bar(
    risk_analysis,
    x="total_risk_score",
    y="fraud_rate",
    title="Fraud Rate (%) by Risk Score",
    labels={"fraud_rate": "Fraud Rate (%)"}
)

st.plotly_chart(fig2, use_container_width=True)

# ---- Amount Distribution ----
st.subheader("Transaction Amount Distribution")

fig3 = px.histogram(
    filtered_df,
    x="Amount",
    nbins=50,
    title="Transaction Amount Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

st.success("Dashboard connected live to MotherDuck Cloud 🚀")
