import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul untuk dashboard
st.title('Dashboard Analisis Bike Sharing')

# Memuat dataset dengan st.cache_data
@st.cache_data
def load_data():
    data = pd.read_csv('../data/hour.csv')
    return data

data = load_data()

# Menampilkan dataset
st.write("### Data Bike Sharing", data.head())

# Sidebar untuk parameter input pengguna
st.sidebar.header('Parameter Input Pengguna')

# Select box untuk bulan
selected_month = st.sidebar.selectbox('Bulan', data['mnth'].unique())

# Filter data berdasarkan bulan yang dipilih
filtered_data = data[data['mnth'] == selected_month]

# Menampilkan data yang difilter
st.write(f"### Data untuk Bulan {selected_month}", filtered_data.head())

# Visualisasi: Jumlah Pengguna per Jam
st.write("### Jumlah Pengguna per Jam")
fig, ax = plt.subplots()
ax.plot(filtered_data['hr'], filtered_data['cnt'], 'b-', label='Total Pengguna')
ax.set_xlabel('Jam dalam Sehari')
ax.set_ylabel('Jumlah Pengguna')
st.pyplot(fig)
