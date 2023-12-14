import random

def gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero):
    grupos = []

    for _ in range(n_grupos):
        grupo = random.sample(range(min_numero, max_numero + 1), n_numeros_por_grupo)
        grupo.sort()  # Ordena os números em ordem crescente
        grupos.append(grupo)

    return grupos

def imprimir_grupos(grupos):
    for i, grupo in enumerate(grupos, start=1):
        grupo_formatado = [f'{num:02}' for num in grupo]
        print(f'Jogo {i}: {", ".join(grupo_formatado)}')

if __name__ == "__main__":
    n_grupos = 5  # Altere o número de grupos conforme necessário
    n_numeros_por_grupo = 6
    min_numero = 1
    max_numero = 60

    grupos = gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero)

    imprimir_grupos(grupos)
