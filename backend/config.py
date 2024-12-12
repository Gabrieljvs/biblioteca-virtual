# Responsável por criar e configurar a aplicação Flask e o banco de dados.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Função para criar a aplicação e configurar o Flask

def create_app():
    app = Flask(__name__)
    # Configuração da URI do banco de dados (substituir com as credenciais reais)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@host:port/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

# Instância do SQLAlchemy usada em toda a aplicação
db = SQLAlchemy()