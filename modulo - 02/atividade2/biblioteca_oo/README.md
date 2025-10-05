Bem-vindo a Biblioteca, um sistema simples e funcional de gerenciamento da biblioteca desenvolvido em Python.
Com ele, é possível cadastrar usuários, cadastrar livros, realizar emprestimos e devoluçao consultar catalogo de forma prática e organizada.


O objetivo é permitir o sistema gerencie usuários e livors simulando as principais operações de uma biblioteca no dia a dia.

Funcionalidade:

Gerenciamento de Usuários
.Cadastra novos usuários com (nome, ID)
.Cada usuário pode pegar empestado livros

Gerenciamento de livros
.Cadasto novos de livros(titulo, autor, ano)
.Empresta e Devolver livros

Listagem
.Lista Livros e Usuarios


Estrutura de pastas e arquivos:

biblioteca_oo/
├── src/
│   ├── main.py
│   ├── models/
│   │   ├──biblioteca.py
│   │   ├── catalogo.py
│   │   ├── gerenciador_emprestemo.py
│   │   ├── gerenciador_usuarios.py
│   │   ├── livro.py
│   │   └── usuario.py
│   └── utils/
│   │   └── formatadores.py
├── tests/
│   └── test_biblioteca.py
├── requirements.txt
└── README.md


Requisito:
Python 3.10 ou superior instalado em sua máquina.