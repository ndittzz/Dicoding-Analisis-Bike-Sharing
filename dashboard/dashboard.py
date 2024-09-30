import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul untuk dashboard
st.title('Dashboard Analisis Bike Sharing')

# Memuat dataset 'hour.csv' dan 'day.csv' dengan st.cache_data
@st.cache_data
def load_data_hour():
    return pd.read_csv('hour.csv')

@st.cache_data
def load_data_day():
    return pd.read_csv('day.csv')

# Memuat data
hour_data = load_data_hour()
day_data = load_data_day()

# Menampilkan dataset "hour"
st.write("### Data Bike Sharing (Hour)", hour_data.head())

# Sidebar untuk parameter input pengguna
st.sidebar.header('Parameter Input Pengguna')

# Select box untuk bulan (data jam)
selected_month = st.sidebar.selectbox('Bulan (Hour)', hour_data['mnth'].unique())

# Filter data berdasarkan bulan yang dipilih (data jam)
filtered_hour_data = hour_data[hour_data['mnth'] == selected_month]

# Menampilkan data yang difilter (data jam)
st.write(f"### Data untuk Bulan {selected_month} (Hour)", filtered_hour_data.head())

# Visualisasi 1: Jumlah Pengguna per Jam
st.write("### Jumlah Pengguna per Jam")
fig, ax = plt.subplots()
ax.plot(filtered_hour_data['hr'], filtered_hour_data['cnt'], 'b-', label='Total Pengguna')
ax.set_xlabel('Jam dalam Sehari')
ax.set_ylabel('Jumlah Pengguna')
st.pyplot(fig)

# ---- Visualisasi 2: Karakteristik Pengguna yang Berpengaruh terhadap Frekuensi Penyewaan ----
st.write("### Karakteristik Pengguna yang Mempengaruhi Frekuensi Penyewaan (Harian)")

# Select box untuk karakteristik pengguna dari dataset harian (day.csv)
selected_characteristic = st.sidebar.selectbox(
    'Pilih Karakteristik Pengguna (Harian)', 
    ['season', 'weekday', 'weathersit']
)

# Filter dan grup data harian berdasarkan karakteristik yang dipilih
grouped_day_data = day_data.groupby(selected_characteristic)['cnt'].mean().reset_index()

# Visualisasi karakteristik pengguna
fig2, ax2 = plt.subplots()
ax2.bar(grouped_day_data[selected_characteristic], grouped_day_data['cnt'], color='orange')
ax2.set_xlabel(selected_characteristic.capitalize())
ax2.set_ylabel('Rata-rata Jumlah Pengguna')
st.pyplot(fig2)

# Menampilkan ringkasan data karakteristik
st.write(f"### Rata-rata Penyewaan Berdasarkan {selected_characteristic.capitalize()}")
st.write(grouped_day_data)
