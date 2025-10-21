import pandas as pd
from pathlib import Path

class DataBase():
    def __init__(self):
        pass

    def import_file(self):
        script_path = Path(__file__)
        src_dir = script_path.parent
        project_root = src_dir.parent
        csv_file_path = project_root / 'data' / 'vgsales.csv'
        df = pd.read_csv(csv_file_path)

        return df
    
    def clean_data(self):
        df = self.import_file()
        
        if 'Ano' not in df.columns:
            print("Erro: A coluna 'Ano' não foi encontrada no CSV.")
            return df 
        
        print(f"Quantidade de linhas antes: {len(df)}")
        cleaned_df = df.dropna(subset=['Ano'])
        print(f"Quantidade de linhas depois: {len(cleaned_df)}")

        return cleaned_df
    
class DataAnalysis():
    def __init__(self, df):
        self.df = df
        pass

    def sales_and_genre_analysis(self):
        sales = self.df.groupby('Gênero')['Vendas Globais (milhões)'].sum()
        top_genre = sales.idxmax()
        top_sales = sales.max()

        return top_genre, top_sales
    

db = DataBase()
cleaned_date = db.clean_data()

file = DataAnalysis(cleaned_date)

file.sales_and_genre_analysis()