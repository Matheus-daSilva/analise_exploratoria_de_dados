import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

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
        self.df = df.copy()

    def sales_and_genre_analysis(self):
        sales = self.df.groupby('Gênero')['Vendas Globais (milhões)'].sum()
        top_genre = sales.idxmax()
        top_sales = sales.max()

        return top_genre, top_sales
    
    def console_analysis(self):
        console_counts = self.df['Plataforma'].value_counts()
        top_console = console_counts.idxmax()

        return top_console
    
    def decade_classification(self):
        def classify_decade(year):
            if 1990 <= year <= 1999:
                return "Anos 90"
            elif 2000 <= year <= 2009:
                return "Anos 2000"
            elif 2010 <= year:
                return "Anos 2010"
            
        df_with_decade = self.df.copy()
        df_with_decade['Decada'] = df_with_decade['Ano'].apply(classify_decade)
        
        return df_with_decade

class DataVisualization():
    def __init__(self, df):
        self.df = df.copy()

    def plot_top_genres_sales(self):
        genre_sales = self.df.groupby('Gênero')['Vendas Globais (milhões)'].sum().sort_values(ascending=False).head(5)
        plt.figure(figsize=(10, 6))
        genre_sales.plot(kind='bar', color='skyblue')
        
        plt.title('Top 5 Gêneros por Vendas Globais Totais')
        plt.xlabel('Gênero')
        plt.ylabel('Vendas Globais (em Milhões)')
        plt.xticks(rotation=45)
        plt.tight_layout()
       
        plt.show()

    def plot_releases_per_year(self):
        releases_per_year = self.df['Ano'].value_counts().sort_index()
        releases_per_year = releases_per_year.loc[1980:2016] 
        
        plt.figure(figsize=(12, 6))
        releases_per_year.plot(kind='line', marker='o', linestyle='-')
        
        plt.title('Total de Lançamentos de Jogos por Ano (1980-2016)')
        plt.xlabel('Ano')
        plt.ylabel('Número de Jogos Lançados')
        plt.grid(True) # Adiciona uma grade para facilitar a leitura
        plt.tight_layout()
        
        plt.show()    
    

db = DataBase()
cleaned_date = db.clean_data()

file = DataAnalysis(cleaned_date)

image = DataVisualization(cleaned_date)

file.decade_classification()

image.plot_releases_per_year()