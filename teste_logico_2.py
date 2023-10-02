class Node:
    def __init__(self, palavra):
        self.palavra = palavra
        self.esquerda = None
        self.direita = None

def inserir(raiz, palavra):
    if raiz is None:
        return Node(palavra)
    elif palavra < raiz.palavra:
        raiz.esquerda = inserir(raiz.esquerda, palavra)
    elif palavra > raiz.palavra:
        raiz.direita = inserir(raiz.direita, palavra)
    return raiz

def buscar(raiz, palavra, caminho=[]):
    if raiz is None:
        return []
    
    caminho.append(raiz.palavra)

    if raiz.palavra == palavra:
        return caminho
    elif palavra < raiz.palavra:
        return buscar(raiz.esquerda, palavra, caminho)
    else:
        return buscar(raiz.direita, palavra, caminho)


arvore = None
palavras = ["maça", "morango", "goiaba", "laranja", "uva", "banana"]
for palavra in palavras:
    arvore = inserir(arvore, palavra)

palavra_chave = str(input("Temos as seguintes frutas:\n Maçã, morango, goiaba, laranja, uva, banana\nQual fruta você quer encontrar? "))
caminho_encontrado = buscar(arvore, palavra_chave)

if caminho_encontrado:
    caminho_str = " -> ".join(caminho_encontrado)
    print(f"Caminho até {palavra_chave}: {caminho_str}")
else:
    print(f"{palavra_chave} não encontrado na árvore.")
