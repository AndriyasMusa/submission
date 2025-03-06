import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Mengload Data 
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/kualitas.csv", parse_dates=["date"])
    return df

df = load_data()

forecast_df = pd.read_csv("dashboard/forecast.csv", parse_dates=["date"])

# Buat Filterisasi (sidebar)
st.sidebar.header("Filter Dulu Bang Dicoding")
## Filter untuk Stasiun
st.sidebar.subheader("Filter Stasiun")
selected_station = st.sidebar.selectbox("Pilih Stasiun", df["station"].unique())

## Filter untuk Periode
st.sidebar.subheader("Filter Periode")
start_date = st.sidebar.date_input("Dari", df["date"].min())
end_date = st.sidebar.date_input("Sampai", df["date"].max())

filtered_df = df[
    (df["station"] == selected_station) &
    (df["date"] >= pd.to_datetime(start_date)) &
    (df["date"] <= pd.to_datetime(end_date))
]
filtered_forecast_df = forecast_df[forecast_df["station"] == selected_station]

# Tampilan Utama (mainbar)
st.title("Dashboard Kualitas Udara")

## Tren Perubahan PM2.5 dan PM10
st.subheader("Tren Perubahan PM2.5 dan PM10")
fig = px.line(filtered_df, x="date", y=["PM2.5", "PM10"], title="Tren PM2.5 & PM10", markers=True)
st.plotly_chart(fig)

## Tren Perubahan Kandungan SO2, NO2, CO, O3 
st.subheader("Tren SO2, NO2, CO, dan O3")
fig = px.line(filtered_df, x="date", y=["SO2", "NO2", "CO", "O3"], 
               title="Tren Kandungan Patikel (SO2, NO2, CO, O3)", markers=True)
st.plotly_chart(fig)

## Scatter Plot  Hubungan Suhu Udara dan Curah Hujan terhadap PM2.5
st.subheader("Hubungan Suhu Udara dan Curah Hujan terhadap PM2.5")

fig, ax = plt.subplots(figsize=(8, 6))

sc = ax.scatter(
    filtered_df["RAIN"], filtered_df["PM2.5"],
    c=filtered_df["TEMP"], cmap="coolwarm", alpha=0.7, edgecolors="w"
)

ax.set_title("RAIN & TEMP vs PM2.5")
ax.set_xlabel("Curah Hujan (RAIN)")
ax.set_ylabel("Konsentrasi Partikel (PM2.5)")
ax.grid(True)

cbar = plt.colorbar(sc)
cbar.set_label("Suhu Udara (TEMP)")

st.pyplot(fig)  

## Scatter Plot  Hubungan Suhu Udara dan Titik Embun terhadap PM2.5
st.subheader("Hubungan Tekanan Udara dan Titik Embun terhadap PM2.5")

fig, ax = plt.subplots(figsize=(8, 6))

sc = ax.scatter(
    filtered_df["PRES"], filtered_df["PM2.5"],
    c=filtered_df["DEWP"], cmap="coolwarm", alpha=0.7, edgecolors="w"
)

ax.set_title("RAIN & TEMP vs PM2.5")
ax.set_xlabel("Curah Hujan (RAIN)")
ax.set_ylabel("Konsentrasi Partikel (PM2.5)")
ax.grid(True)

cbar = plt.colorbar(sc)
cbar.set_label("Suhu Udara (TEMP)")

st.pyplot(fig)  

## Heatmap korelasi
st.subheader("Korelasi Antar Variabel")
correlation = filtered_df[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "TEMP", "RAIN","PRES","DEWP"]].corr()
st.write(correlation.style.background_gradient(cmap="coolwarm"))

st.write("Muhammad Andriyas Musa Munthalib MC011D5Y1281")


## Hasil Forecast PM2.5
st.subheader("Hasil Forecast PM2.5")
fig = px.line(filtered_forecast_df, x="date", y=["actual", "forecast"], 
              title=f"Forecast PM2.5 - {selected_station}", markers=True)
st.plotly_chart(fig)