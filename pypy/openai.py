import random

def gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero):
    if not (0 < n_grupos <= (max_numero - min_numero + 1) // n_numeros_por_grupo):
        raise ValueError("Número de grupos inválido")

    numeros_disponiveis = []
    grupos = []

    for _ in range(n_grupos):
        # sempre que esgotar os numeros, reinicia
        if len(numeros_disponiveis) < n_numeros_por_grupo:
            numeros_disponiveis = list(range(min_numero, max_numero + 1))

        numeros_grupo = random.sample(numeros_disponiveis, n_numeros_por_grupo)
        numeros_grupo.sort()
        grupos.append(numeros_grupo)

        # Remove os números já escolhidos para evitar repetição
        numeros_disponiveis = list(set(numeros_disponiveis) - set(numeros_grupo))

    return grupos

def imprimir_grupos(grupos):
    for i, grupo in enumerate(grupos, start=1):
        grupo_formatado = [f'{num:02}' for num in grupo]
        print(f'Jogo {i}: {", ".join(grupo_formatado)}')


def coletar_valores_entrada():
    try:
        n_grupos = int(input("Digite o número de grupos desejado: "))
        n_numeros_por_grupo = int(input("Digite o número de números por grupo: "))
        min_numero = int(input("Digite o número mínimo disponível: "))
        max_numero = int(input("Digite o número máximo disponível: "))

        grupos = gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero)
        imprimir_grupos(grupos)
        exit()

    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    coletar_valores_entrada()
    n_grupos = 5  # Altere o número de grupos conforme necessário
    n_numeros_por_grupo = 6
    min_numero = 1
    max_numero = 60

    grupos = gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero)

    imprimir_grupos(grupos)