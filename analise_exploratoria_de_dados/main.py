from src.controller import DataBase, DataAnalysis, DataVisualization

db = DataBase()

data_analisys = DataAnalysis(db.clean_data())
sales = data_analisys.sales_and_genre_analysis()
console = data_analisys.console_analysis()
decade_classification = data_analisys.decade_classification()

data_visualization = DataVisualization(decade_classification, sales, console)
data_visualization.plot_top_genres_sales()
data_visualization.plot_releases_per_year()

print(data_visualization.generate_conclusion())