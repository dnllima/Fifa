import pyodbc
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter variáveis de ambiente para a conexão com o banco de dados
driver = os.getenv('DB_DRIVER')
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

# Verificar se todas as variáveis de ambiente foram carregadas corretamente
if not all([driver, server, database, user, password]):
    raise ValueError("Uma ou mais variáveis de ambiente não foram carregadas corretamente. Verifique o arquivo .env.")

# Construir a string de conexão
dados_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}"

# Verificar se a string de conexão foi carregada corretamente
print(f"String de conexão: {dados_conexao}")

try:
    # Tentar conectar usando pyodbc
    connection = pyodbc.connect(dados_conexao)
    print("Conexão com o banco de dados estabelecida com sucesso!")
    connection.close()
except pyodbc.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

    
