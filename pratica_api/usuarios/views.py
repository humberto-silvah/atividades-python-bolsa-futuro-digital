from rest_framework.decorators import api_view
from rest_framework.response import Response

# Banco de dados em memória
produtos = usuarios = [
    {"id": 1, "nome": "Ana", "email": "ana@email.com"}
]

@api_view(["GET"])
def listar_usuarios(request):
    return Response(usuarios)

@api_view(["POST"])
def cadastrar_usuario(request):
    novo = request.data
    novo["id"] = len(usuarios) + 1
    usuarios.append(novo)
    return Response(novo, status=201)