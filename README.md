# Projek Akhir Analisis Data - MC011D5Y1821

## MENJALANKAN NOTEBOOK IPYNB (Lampiran analisis data ke file forecast.csv dan kualits.csv )
### Mengambil data dari Notebook.ipynb (Saya Jalankan di Colab)
```
https://colab.research.google.com/drive/1HbdIqOEm4Gmi8qlB26xxVzsFHMnwT0aX?usp=sharing

# Jangan lupa untuk mengupload data (data daari dicoding atau data di folder(data)) ke colab
# Setelah upload, lalu jalankan semuanya, kemudian tampil pop up file baru kualitas.csv dan forecast.csv
# Download ke internal 

```
## MENJALANKAN DASHBOARD
### Setup Environment terminal
```
# buat virtual environment di folder submission
mkdir submission
cd submission
pip env install
pipenv shell

# install package yang digunakan
pip install numpy pandas matplotlib seaborn babel plotly streamlit

```

### Membuat folder dashboard
```
# folder dashboard berisikan dashboard.py dan kualitas.csv serta forecast.csv
```

### Membuat Folder Data 
```
# Folder data berisikan data dari dicoding, ada 12 data stasiun air quality
```

### Menjalankan Dashboard
```
streamlit run dashboard/dashboard.py
```
