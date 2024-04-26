# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Criar a engine, que é o ponto de entrada do SQLAlchemy para interações com o banco de dados
engine = create_engine(DATABASE_URI, echo=True)  # O parâmetro echo=True é útil para debugging.

# Criar uma sessão configurada que é a interface para o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if __name__ == '__main__':
    try:
        # Tentar conectar ao banco de dados
        connection = engine.connect()
        print("Conexão bem-sucedida!")
        # Tentar executar uma query simples
        result = connection.execute("SELECT * FROM attribute_weights LIMIT 1;")
        for row in result:
            print(row)
        # Fechar a conexão
        connection.close()
    except Exception as e:
        print("Ocorreu um erro ao conectar ao banco de dados:", e)


    