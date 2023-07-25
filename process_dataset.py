import pandas as pd
from process_datakelas import *

# #mengambil semua variabel dari file datakelas
# kelas()
# apollo_banyak_tugas_intro_ai = apollo_banyak_tugas_intro_ai
# # apollo_banyak_tugas_python = apollo_banyak_tugas_python
# # apollo_banyak_tugas_siklus = apollo_banyak_tugas_siklus
# # apollo_banyak_tugas_intro_ml = apollo_banyak_tugas_intro_ml

# #global variabel agar bisa diakses diluar file
# global df, df_nama, size, df_avg_tugas_intro_ai

# def load():
#     global df, df_nama, size, df_avg_tugas_intro_ai

#     #input database
#     dir = "database/database.xlsx"

#     df_datasiswa = pd.read_excel(dir, sheet_name="datasiswa")

#     #drop column nama pada sheet intro_ai, karena akan disambungkan dengan dataframe utama
#     df1 = pd.read_excel(dir, sheet_name="intro_ai")
#     df1 = df1.drop(['nama'], axis=1)

#     #drop column nama pada sheet python, karena akan disambungkan dengan dataframe utama
#     df2 = pd.read_excel(dir, sheet_name="python")
#     df2 = df2.drop(['nama'], axis=1)

#     #penggabungan antar dataframe menjadi 1 dataframe utama
#     df = pd.concat([df_datasiswa, df1, df2], axis=1)

#     #membuat list nama, untuk membuat selectbox pada inputan user
#     df_nama = list(df['nama'])

#     #mengecilkan semua huruf agar nanti ketika diperbandingan akan serupa
#     df['nama'] = df['nama'].str.lower()
#     df['email'] = df['email'].str.lower()

#     #mencari nilai avg pada intro to ai
#     df_avg_tugas_intro_ai = df.iloc[:,4:9].sum(axis=1)
#     df_avg_tugas_intro_ai = df_avg_tugas_intro_ai / apollo_banyak_tugas_intro_ai
#     df.insert(9, 'avg_tugas_intro', df_avg_tugas_intro_ai)

#     # #mencari nilai avg pada python
#     # df_avg_tugas_intro_ai = df.iloc[:,4:9].sum(axis=1)
#     # df_avg_tugas_intro_ai = df_avg_tugas_intro_ai / apollo_banyak_tugas_intro_ai
#     # df.insert(9, 'avg_tugas_intro', df_avg_tugas_intro_ai)

#     # #mencari nilai avg pada siklus
#     # df_avg_tugas_intro_ai = df.iloc[:,4:9].sum(axis=1)
#     # df_avg_tugas_intro_ai = df_avg_tugas_intro_ai / apollo_banyak_tugas_intro_ai
#     # df.insert(9, 'avg_tugas_intro', df_avg_tugas_intro_ai)

#     # #mencari nilai avg pada intro to ml
#     # df_avg_tugas_intro_ai = df.iloc[:,4:9].sum(axis=1)
#     # df_avg_tugas_intro_ai = df_avg_tugas_intro_ai / apollo_banyak_tugas_intro_ai
#     # df.insert(9, 'avg_tugas_intro', df_avg_tugas_intro_ai)

#     #menentukan ukuran baris, sebagai penentu kapan berhenti dari loops
#     size = df.shape
#     size = size[0] - 1

class load_dataset():
    #input database
    dir = "database/database.xlsx"

    apollo_banyak_tugas_intro_ai = kelas()
    apollo_banyak_tugas_intro_ai = apollo_banyak_tugas_intro_ai.kirim_data_banyak_tugas()

    def __init__(self):
        self.df_datasiswa = pd.read_excel(self.dir, sheet_name="datasiswa")

        #drop column nama pada sheet intro_ai, karena akan disambungkan dengan dataframe utama
        self.df1 = pd.read_excel(self.dir, sheet_name="intro_ai")
        

        #drop column nama pada sheet python, karena akan disambungkan dengan dataframe utama
        self.df2 = pd.read_excel(self.dir, sheet_name="python")
        self.df2 = self.df2.drop(['nama'], axis=1)

        #penggabungan antar dataframe menjadi 1 dataframe utama
        self.df = pd.concat([self.df_datasiswa, self.df1, self.df2], axis=1)

        #membuat list nama, untuk membuat selectbox pada inputan user
        self.df_nama = list(self.df['nama'])



        #mencari nilai avg pada intro to ai
        self.df_avg_tugas_intro_ai = self.df.iloc[:,4:9].sum(axis=1)

        
        

        #menentukan ukuran baris, sebagai penentu kapan berhenti dari loops
        self.size = self.df.shape
        self.size = self.size[0] - 1

    def kirim_data_dataset(self):
        #mengecilkan semua huruf agar nanti ketika diperbandingan akan serupa
        # self.df['nama'] = self.df['nama'].str.lower()
        # self.df['email'] = self.df['email'].str.lower()

        self.df_avg_tugas_intro_ai = self.df_avg_tugas_intro_ai / self.apollo_banyak_tugas_intro_ai
        self.df.insert(9, 'avg_tugas_intro', self.df_avg_tugas_intro_ai)

        return self.df, self.df_nama, self.size
    