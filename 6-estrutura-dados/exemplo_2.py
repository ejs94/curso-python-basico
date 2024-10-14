# Criando um dicionário com informações sobre um livro
livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899,
    "genero": "Romance"
}

# Exibindo o título do livro
print("Título:", livro["titulo"])  # Saída: Título: Dom Casmurro

# Adicionando uma nova chave ao dicionário
livro["em_estoque"] = True

# Exibindo o dicionário completo
print("Informações do livro:", livro)

# Acessando e exibindo um valor específico
print("Autor:", livro["autor"])  # Saída: Autor: Machado de Assis

# Atualizando o ano de publicação
livro["ano"] = 1900
print("Ano atualizado:", livro["ano"])  # Saída: Ano atualizado: 1900
