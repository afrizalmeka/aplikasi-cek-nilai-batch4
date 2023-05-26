import pandas as pd
from process_datakelas import *

#mengambil semua variabel dari file datakelas
kelas()
apollo_banyak_tugas_intro_ai = apollo_banyak_tugas_intro_ai
apollo_banyak_tugas_python = apollo_banyak_tugas_python
apollo_banyak_tugas_siklus = apollo_banyak_tugas_siklus
apollo_banyak_tugas_intro_ml = apollo_banyak_tugas_intro_ml

#global variabel agar bisa diakses diluar file
global df, df_nama, size, df_avg_tugas_intro_ai

def load():
    global df, df_nama, size, df_avg_tugas_intro_ai

    #input database
    dir = "database/database.xlsx"

    df_datasiswa = pd.read_excel(dir, sheet_name="datasiswa")

    #drop column nama pada sheet intro_ai, karena akan disambungkan dengan dataframe utama
    df1 = pd.read_excel(dir, sheet_name="intro_ai")
    df1 = df1.drop(['nama'], axis=1)

    #drop column nama pada sheet python, karena akan disambungkan dengan dataframe utama
    df2 = pd.read_excel(dir, sheet_name="python")
    df2 = df2.drop(['nama'], axis=1)

    #penggabungan antar dataframe menjadi 1 dataframe utama
    df = pd.concat([df_datasiswa, df1, df2], axis=1)

    #membuat list nama, untuk membuat selectbox pada inputan user
    df_nama = list(df['nama'])

    #mengecilkan semua huruf agar nanti ketika diperbandingan akan serupa
    df['nama'] = df['nama'].str.lower()
    df['email'] = df['email'].str.lower()

    #mencari nilai avg pada intro to ai
    df_avg_tugas_intro_ai = df.iloc[:,4:9].sum(axis=1)
    df_avg_tugas_intro_ai = df_avg_tugas_intro_ai / apollo_banyak_tugas_intro_ai
    df.insert(9, 'avg_tugas_intro', df_avg_tugas_intro_ai)

    # #mencari nilai avg pada python
    # df_avg_tugas_intro_ai = df.iloc[:,4:9].sum(axis=1)
    # df_avg_tugas_intro_ai = df_avg_tugas_intro_ai / apollo_banyak_tugas_intro_ai
    # df.insert(9, 'avg_tugas_intro', df_avg_tugas_intro_ai)

    # #mencari nilai avg pada siklus
    # df_avg_tugas_intro_ai = df.iloc[:,4:9].sum(axis=1)
    # df_avg_tugas_intro_ai = df_avg_tugas_intro_ai / apollo_banyak_tugas_intro_ai
    # df.insert(9, 'avg_tugas_intro', df_avg_tugas_intro_ai)

    # #mencari nilai avg pada intro to ml
    # df_avg_tugas_intro_ai = df.iloc[:,4:9].sum(axis=1)
    # df_avg_tugas_intro_ai = df_avg_tugas_intro_ai / apollo_banyak_tugas_intro_ai
    # df.insert(9, 'avg_tugas_intro', df_avg_tugas_intro_ai)

    #menentukan ukuran baris, sebagai penentu kapan berhenti dari loops
    size = df.shape
    size = size[0] - 1