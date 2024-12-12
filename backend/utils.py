# Funções auxiliares reutilizáveis.
from flask import jsonify

# Função para criar uma resposta de erro padronizada.
def response_error(message, status_code):
    return jsonify({'error': message}), status_code
