import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Visualisasi 1: Jumlah Pengguna per Jam (Sederhana)
st.write("### Jumlah Pengguna per Jam")

# Menggunakan bar chart untuk menampilkan jumlah pengguna per jam
fig, ax = plt.subplots()
ax.bar(filtered_hour_data['hr'], filtered_hour_data['cnt'], color='skyblue')  # Menggunakan bar chart
ax.set_xlabel('Jam dalam Sehari')  # Menambahkan label sumbu X
ax.set_ylabel('Jumlah Pengguna')  # Menambahkan label sumbu Y
ax.set_title('Jumlah Pengguna per Jam dalam Sehari (Bar Chart)')  # Judul yang lebih jelas
st.pyplot(fig)

# Menambahkan label keterangan yang lebih jelas
st.write("Grafik ini menunjukkan perubahan jumlah pengguna sepeda di setiap jam dalam sehari untuk bulan yang dipilih.")

# ---- Visualisasi 2: Karakteristik Pengguna Berdasarkan Pilihan Pengguna (Seaborn Box Plot) ----
st.write("### Frekuensi Penyewaan Berdasarkan Karakteristik Pengguna (Data Harian)")

# Select box untuk memilih karakteristik pengguna (misalnya: weekday, season, dll.)
selected_day_characteristic = st.sidebar.selectbox(
    'Pilih Karakteristik Pengguna untuk Visualisasi', 
    ['weekday', 'season', 'weathersit']  # Pilihan input pengguna
)

# Visualisasi menggunakan seaborn (karakteristik pengguna yang dipilih)
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_data, x=selected_day_characteristic, y='cnt', ax=ax4)
ax4.set_title(f'Frekuensi Penyewaan Berdasarkan {selected_day_characteristic.capitalize()} (Data Harian)')
ax4.set_xlabel(selected_day_characteristic.capitalize())
ax4.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig4)

