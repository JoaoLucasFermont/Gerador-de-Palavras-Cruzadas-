import random

# Definir palavras e dicas
palavras = {
    "cachorro": "Animal de estimação",
    "gato": "Animal doméstico",
    "banana": "Fruta amarela",
    "carro": "Meio de transporte",
    "casa": "Moradia"
}


# Função para criar uma grade vazia
def criar_grade(tamanho):
    grade = []
    for _ in range(tamanho):
        linha = [' '] * tamanho
        grade.append(linha)
    return grade


# Função para inserir palavra na grade horizontalmente
def inserir_palavra_horizontal(grade, palavra, linha, coluna):
    for i in range(len(palavra)):
        grade[linha][coluna + i] = palavra[i]


# Função para inserir palavra na grade verticalmente
def inserir_palavra_vertical(grade, palavra, linha, coluna):
    for i in range(len(palavra)):
        grade[linha + i][coluna] = palavra[i]


# Função para exibir a grade de palavras cruzadas
def exibir_grade(grade):
    for linha in grade:
        print(' '.join(linha))


# Função para preencher espaços em branco com letras aleatórias
def preencher_espacos(grade):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(grade)):
        for j in range(len(grade[i])):
            if grade[i][j] == ' ':
                grade[i][j] = random.choice(letras)


# Função principal
def main():
    tamanho_grade = 10
    grade = criar_grade(tamanho_grade)

    for palavra, dica in palavras.items():
        direcao = random.choice(['horizontal', 'vertical'])
        if direcao == 'horizontal':
            linha = random.randint(0, tamanho_grade - 1)
            coluna = random.randint(0, tamanho_grade - len(palavra))
            inserir_palavra_horizontal(grade, palavra, linha, coluna)
        else:
            linha = random.randint(0, tamanho_grade - len(palavra))
            coluna = random.randint(0, tamanho_grade - 1)
            inserir_palavra_vertical(grade, palavra, linha, coluna)

    preencher_espacos(grade)
    exibir_grade(grade)


if __name__ == "__main__":
    main()
