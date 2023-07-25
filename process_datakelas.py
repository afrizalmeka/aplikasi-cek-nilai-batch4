import pandas as pd

# global df_kelas, apollo_banyak_tugas_intro_ai, apollo_banyak_pertemuan_intro_ai, apollo_banyak_tugas_python, apollo_banyak_pertemuan_python, apollo_banyak_tugas_siklus, apollo_banyak_pertemuan_siklus, apollo_banyak_tugas_intro_ml, apollo_banyak_pertemuan_intro_ml

# def kelas():
#     global df_kelas, apollo_banyak_tugas_intro_ai, apollo_banyak_pertemuan_intro_ai, apollo_banyak_tugas_python, apollo_banyak_pertemuan_python, apollo_banyak_tugas_siklus, apollo_banyak_pertemuan_siklus, apollo_banyak_tugas_intro_ml, apollo_banyak_pertemuan_intro_ml

#     dir = "database/informasi_kelas.xlsx"

#     df_kelas = pd.read_excel(dir, sheet_name="datakelas")

#     #Logika dan Konsep Teknologi AI
#     apollo_banyak_tugas_intro_ai = int(df_kelas.iloc[0, 1])
#     apollo_banyak_pertemuan_intro_ai = int(df_kelas.iloc[0, 5])

#     #Pemrograman Python
#     apollo_banyak_tugas_python = int(df_kelas.iloc[0, 2])
#     apollo_banyak_pertemuan_python = int(df_kelas.iloc[0, 6])

#     #Siklus Proyek AI
#     apollo_banyak_tugas_siklus = int(df_kelas.iloc[0, 3])
#     apollo_banyak_pertemuan_siklus = int(df_kelas.iloc[0, 7])

#     #Metode Penelitian AI - Machine Learning Dasar
#     apollo_banyak_tugas_intro_ml = int(df_kelas.iloc[0, 4])
#     apollo_banyak_pertemuan_intro_ml = int(df_kelas.iloc[0, 8])

class kelas():
    dir = "database/informasi_kelas.xlsx"
    
    def __init__(self):
        self.df_kelas = pd.read_excel(self.dir, sheet_name="datakelas")

        #Logika dan Konsep Teknologi AI
        self.apollo_banyak_tugas_intro_ai = int(self.df_kelas.iloc[0, 1])
        self.apollo_banyak_pertemuan_intro_ai = int(self.df_kelas.iloc[0, 5])

        # #Pemrograman Python
        # self.apollo_banyak_tugas_python = int(df_kelas.iloc[0, 2])
        # self.apollo_banyak_pertemuan_python = int(df_kelas.iloc[0, 6])

        # #Siklus Proyek AI
        # self.apollo_banyak_tugas_siklus = int(df_kelas.iloc[0, 3])
        # self.apollo_banyak_pertemuan_siklus = int(df_kelas.iloc[0, 7])

        # #Metode Penelitian AI - Machine Learning Dasar
        # self.apollo_banyak_tugas_intro_ml = int(df_kelas.iloc[0, 4])
        # self.apollo_banyak_pertemuan_intro_ml = int(df_kelas.iloc[0, 8])
    
    def kirim_data_banyak_tugas(self):
        return self.apollo_banyak_tugas_intro_ai