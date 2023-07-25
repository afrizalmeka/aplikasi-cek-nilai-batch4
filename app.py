import streamlit as st
import pandas as pd
from process_dataset import *

# #Memanggil semua variabel dataset yang diperlukan
# load()
# df_nama = df_nama

process = load_dataset()
df, df_nama, size = process.kirim_data_dataset()

#Header Aplikasi
st.title('Aplikasi Cek Nilai Apollo Class')
st.caption('Batch 4 - Power Academy')

st.text("\n")
st.text("\n")


# Memulai Inputan Data
#Inputan Nama
nama = st.selectbox(
    'Nama Lengkap :',
    (df_nama))

#Inputan ID MSIB
id_msib = st.number_input("ID MSIB : ", min_value=0)

#Inputan No HP
nohp = st.number_input("No HP : ", min_value=0)

#Inputan Email
email = st.text_input("Email : ")

#wadah untuk inputan
data = []

#menambah value di lisr "data"
#tujuan lowercase pada string, supaya agar kecil semua huruf nya. untuk keperluan validasi
data.append(str(nama).lower().strip())
data.append(int(id_msib))
data.append(int(nohp))
data.append(str(email).lower().strip())



#Tombol untuk validasi data inputan dengan database
if st.button('Submit'):
    for x in df.index:
        A = df['nama'][x]
        B = df['id_msib'][x]
        C = df['nohp'][x]
        D = df['email'][x]
        

        #memvalidasi apakah nama, id_msib, univ, prodi, nohp sesuai atau tidak
        if (data[0] == A) and (data[1] == B) and (data[2] == C) and (data[3] == D):
            st.success("Data telah ditemukan")

            st.text("\n")
            st.text("\n")

            #Tampilan Materi Intro to AI
            st.subheader("Logika dan Konsep Teknologi AI")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Banyak Tugas : ")

            with col2:
                df_tugas_intro = df.iloc[x, 4:10].astype(float)
                df_tugas_intro = df_tugas_intro.rename({"intro_1": "Tugas 1", "intro_2": "Tugas 2", "intro_3": "Tugas 3", 
                                                        "intro_4": "Tugas 4", "intro_5": "Tugas 5", "avg_tugas_intro": "Rata-rata Tugas"})
                st.table(df_tugas_intro)

            with col3:
                df_absen_intro = df.iloc[x, 10:16].astype(int)
                df_absen_intro = df_absen_intro.rename({"absen_intro_1": "Absen Pertemuan 1", "absen_intro_2": "Absen Pertemuan 2", "absen_intro_3": "Absen Pertemuan 3", 
                                                        "absen_intro_4": "Absen Pertemuan 4", "absen_intro_5": "Absen Pertemuan 5", "jumlah_absen_intro": "Jumlah Absen"})
                st.table(df_absen_intro)

            #Tampilan Materi Pemrograman Python
            st.subheader("Pemrograman Python")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Banyak Tugas : ")

            with col2:
                df_tugas_intro = df.iloc[x, 4:10].astype(float)
                df_tugas_intro = df_tugas_intro.rename({"intro_1": "Tugas 1", "intro_2": "Tugas 2", "intro_3": "Tugas 3", 
                                                        "intro_4": "Tugas 4", "intro_5": "Tugas 5", "avg_tugas_intro": "Rata-rata Tugas"})
                st.table(df_tugas_intro)

            with col3:
                df_absen_intro = df.iloc[x, 10:16].astype(int)
                df_absen_intro = df_absen_intro.rename({"absen_intro_1": "Absen Pertemuan 1", "absen_intro_2": "Absen Pertemuan 2", "absen_intro_3": "Absen Pertemuan 3", 
                                                        "absen_intro_4": "Absen Pertemuan 4", "absen_intro_5": "Absen Pertemuan 5", "jumlah_absen_intro": "Jumlah Absen"})
                st.table(df_absen_intro)

            #akan melakukan break jika sudah berhasil menemukan data nya, dan tidak melanjutkan perulangannya
            break

        elif x == size:
            st.error("Data tidak ditemukan")


