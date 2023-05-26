import pandas as pd

class dataset:
    def __init__(self):
        self.data = pd.read_excel("../database/database.xlsx", sheet_name="datasiswa")

