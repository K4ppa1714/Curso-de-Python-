import pandas as pd
import streamlit as st

st.title("Dashboard de Ventas 2026")

# Cargar los datos
df = pd.read_csv("ventas.csv", parse_dates=["Fecha"])

# --- Filtros ---
st.sidebar.header("Filtros")

region = st.sidebar.selectbox("Región", ["Todas"] + sorted(df["Region"].unique()))
producto = st.sidebar.selectbox("Producto", ["Todos"] + sorted(df["Producto"].unique()))

if region != "Todas":
    df = df[df["Region"] == region]

if producto != "Todos":
    df = df[df["Producto"] == producto]

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("Ventas totales", f"${df['Ventas'].sum():,.0f}")
col2.metric("Ticket promedio", f"${df['Ventas'].mean():,.0f}")
col3.metric("Unidades vendidas", f"{df['Cantidad'].sum():,.0f}")

# --- Comparación: ventas por región ---
st.subheader("Ventas por región")
ventas_region = df.groupby("Region")["Ventas"].sum()
st.bar_chart(ventas_region)

# --- Tendencia: ventas por mes ---
st.subheader("Ventas por mes")
df["Mes"] = df["Fecha"].dt.to_period("M").astype(str)
ventas_mes = df.groupby("Mes")["Ventas"].sum()
st.line_chart(ventas_mes)

# --- Evidencia: ventas por producto ---
st.subheader("Ventas por producto")
ventas_producto = df.groupby("Producto")["Ventas"].sum().sort_values(ascending=False)
st.bar_chart(ventas_producto)
