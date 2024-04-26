# test_connection.py

from database import SessionLocal, engine

# Tentar conectar ao banco de dados e fechar a conexão
try:
    # Conectar ao banco de dados
    connection = engine.connect()
    print("Conexão bem sucedida!")
    # Fechar a conexão
    connection.close()
except Exception as e:
    print("Ocorreu um erro ao conectar ao banco de dados:", e)
