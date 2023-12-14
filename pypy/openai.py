import random

def gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero):
    grupos = []

    for _ in range(n_grupos):
        grupo = random.sample(range(min_numero, max_numero + 1), n_numeros_por_grupo)
        grupos.append(grupo)

    return grupos

def imprimir_grupos(grupos):
    for i, grupo in enumerate(grupos, start=1):
        print(f'Jogo {i}: {grupo}')

if __name__ == "__main__":
    n_grupos = 5  # Altere o número de grupos conforme necessário
    n_numeros_por_grupo = 6
    min_numero = 1
    max_numero = 60

    grupos = gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero)

    imprimir_grupos(grupos)
