import pandas as pd
from pathlib import Path

class DataBase():

    def import_file(self):

        script_path = Path(__file__)

        src_dir = script_path.parent

        project_root = src_dir.parent

        csv_file_path = project_root / 'data' / 'vgsales.csv'

        df = pd.read_csv(csv_file_path)

        return df


file = DataBase()
print(file.import_file())