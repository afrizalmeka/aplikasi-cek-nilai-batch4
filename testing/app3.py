import pandas as pd

class dataset():
    def __init__(self):
        self.data = pd.read_excel("../database/database.xlsx", sheet_name="datasiswa")

class data_1():
    def __init__(self):
        self.info = "Berhasil"
        self.berhasil = "OK"

    def say_info(self):
        return self.info, self.berhasil

