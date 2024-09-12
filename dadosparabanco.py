import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from dotenv import load_dotenv
from dados_fifa import df_fifa
from testedeconexao import dados_conexao

# Carregar variáveis de ambiente
load_dotenv()

# Obter os dados do .env
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
driver = os.getenv("DB_DRIVER")

# Verificar se todas as variáveis foram carregadas corretamente
if not all([username, password, host, database, driver]):
    raise ValueError("Uma ou mais variáveis de conexão não foram encontradas no .env")

# Criar a string de conexão usando o SQLAlchemy URL
connection_string = URL.create(
    "mssql+pyodbc",
    username=username,
    password=password,
    host=host,
    database=database,
    query={"driver": driver}
)

# Criar uma conexão com o banco de dados usando SQLAlchemy
engine = create_engine(connection_string)

# enviado os dados para o sql

try:
    df_fifa.to_sql('BD_FIFA', con=engine, if_exists='replace', index=False)
    print("Tabela criada e dados enviados com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao criar a tabela e enviar os dados: {e}")