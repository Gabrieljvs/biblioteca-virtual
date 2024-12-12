from .config import create_app, db
from .routes.livros import livros_bp

# Criação da aplicação Flask.
app = create_app()
# Inicializa o SQLAlchemy com a aplicação.
db.init_app(app)

# Registra os Blueprints das rotas.
app.register_blueprint(livros_bp)

if __name__ == '__main__':
    # Garante que as tabelas sejam criadas no banco de dados ao iniciar o app.
    with app.app_context():
        db.create_all()
    # Executa a aplicação no modo de depuração.
    app.run(debug=True)