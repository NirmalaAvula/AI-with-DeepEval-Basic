import pandas as pd

def load_all_sheets(file_path):

    all_sheets = pd.read_excel(file_path, sheet_name=None)

    return all_sheets