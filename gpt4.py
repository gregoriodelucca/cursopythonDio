import openai
import pandas as pd

# Chave da API OpenAI
openai.api_key = "sua-chave-da-api"

# Função para gerar consulta SQL usando GPT-4
def gerar_sql(descricao):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Gerar uma consulta SQL baseada na seguinte descrição: {descricao}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Exemplo de uso
descricao = "Selecione os nomes, idades e e-mails de todos os clientes da tabela 'clientes' onde a idade é maior que 30."
consulta_sql = gerar_sql(descricao)
print("Consulta gerada:", consulta_sql)

# Usando a consulta gerada para extrair dados
# Supondo que você tenha uma conexão com o banco de dados (exemplo com SQLAlchemy)
import sqlite3

conn = sqlite3.connect('banco_de_dados.db')
df = pd.read_sql_query(consulta_sql, conn)
print(df.head())
