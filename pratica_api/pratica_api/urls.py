from django.contrib import admin
from django.urls import path
from produtos.views import listar_produtos, criar_produto
from usuarios.views import listar_usuarios, cadastrar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),

    path("produtos/", listar_produtos),
    path("produtos/criar/", criar_produto),

    path("usuarios/", listar_usuarios),
    path("usuarios/cadastrar/", cadastrar_usuario),
]