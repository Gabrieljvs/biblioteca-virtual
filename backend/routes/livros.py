# Rotas relacionadas à entidade Livro.
from flask import Blueprint, request, jsonify
from ..models import Livro, db
from ..utils import response_error

# Blueprint para agrupar as rotas de livros.
livros_bp = Blueprint('livros', __name__)

# Rota para criar um novo livro.
@livros_bp.route('/livros', methods=['POST'])
def criar_livro():
    dados = request.json
    # Verifica se os campos obrigatórios foram enviados.
    if not all(k in dados for k in ('titulo', 'autor', 'ano')):
        return response_error('Dados incompletos para criar um livro.', 400)
    try:
        # Cria um novo livro e salva no banco de dados.
        novo_livro = Livro(titulo=dados['titulo'], autor=dados['autor'], ano=dados['ano'])
        db.session.add(novo_livro)
        db.session.commit()
        return jsonify({'message': 'Livro criado com sucesso!', 'id': novo_livro.id}), 201
    except Exception:
        db.session.rollback()
        return response_error('Erro ao criar livro.', 400)

# Rota para listar todos os livros cadastrados.
@livros_bp.route('/livros', methods=['GET'])
def listar_livros():
    livros = Livro.query.all()
    # Retorna uma lista com os livros em formato JSON.
    return jsonify([{'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor, 'ano': livro.ano} for livro in livros])

# Rota para atualizar os dados de um livro existente.
@livros_bp.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    dados = request.json
    livro = Livro.query.get_or_404(id)  # Verifica se o livro existe.
    # Atualiza os campos informados no JSON.
    livro.titulo = dados.get('titulo', livro.titulo)
    livro.autor = dados.get('autor', livro.autor)
    livro.ano = dados.get('ano', livro.ano)
    db.session.commit()
    return jsonify({'message': 'Livro atualizado com sucesso!'})

# Rota para deletar um livro pelo ID.
@livros_bp.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livro = Livro.query.get_or_404(id)  # Verifica se o livro existe.
    db.session.delete(livro)
    db.session.commit()
    return jsonify({'message': 'Livro deletado com sucesso!'})