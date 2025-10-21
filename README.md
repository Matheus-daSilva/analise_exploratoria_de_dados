# Análise Exploratória de Vendas de Videogames

## Descrição do Projeto

Este projeto foi desenvolvido para a equipe de dados de uma empresa de análise de mercado de games. O objetivo é realizar uma análise exploratória (EDA) em um conjunto de dados sobre vendas de videogames (`vgsales.csv`) para extrair insights iniciais e entender as tendências do mercado.

O script automatiza as seguintes tarefas:

* **Carregamento e Limpeza:** Carrega os dados do CSV e limpa o conjunto de dados, removendo linhas com dados de ano ausentes.
* **Análise de Dados:**
    * Identifica o gênero de jogo mais vendido globalmente.
    * Identifica a plataforma (console) com o maior número de jogos lançados.
    * Classifica os jogos por década (Anos 90, 2000, 2010+) para análise de tendências.
* **Visualização e Conclusão:**
    * Gera um gráfico de barras com os 5 gêneros mais vendidos.
    * Gera um gráfico de linhas mostrando o total de lançamentos de jogos por ano.
    * Imprime uma conclusão resumida no terminal com os principais insights encontrados.

## Como Executar

### Pré-requisitos

* Python 3.x
* Bibliotecas Python: `pandas` e `matplotlib`

### Instalação

1.  Clone este repositório ou baixe os arquivos do projeto.

2.  (Recomendado) Crie e ative um ambiente virtual:
    ```bash
    # No macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # No Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  Instale as dependências necessárias:
    ```bash
    pip install pandas matplotlib
    ```

### Execução

Para rodar a análise completa, execute o script `main.py` a partir da pasta raiz do projeto:

```bash
python main.py
