import random
import requests

def obter_semente_aleatoria():
    try:
        response = requests.get("https://www.random.org/integers/?num=1&min=1&max=1000000000&col=1&base=10&format=plain&rnd=new")
        response.raise_for_status()
        seed = int(response.text.strip())
        return seed
    except requests.RequestException as e:
        print(f"Erro ao obter a semente aleatória: {e}")
        return None
    
def obter_bytes_aleatorios(length=64):
    try:
        response = requests.get(f"https://www.random.org/cgi-bin/randbyte?nbytes={length}&format=h")
        response.raise_for_status()
        bytes_aleatorios = bytes.fromhex(''.join(response.text.strip().split()))
        return bytes_aleatorios
    except requests.RequestException as e:
        print(f"Erro ao obter bytes aleatórios: {e}")
        return None
    except ValueError:
        print(f"Erro ao obter bytes aleatórios.")
        return None

def gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero, seed=None):
    if not (0 < n_grupos <= (max_numero - min_numero + 1) // n_numeros_por_grupo):
        raise ValueError("Número de grupos inválido")
    
    if seed is None:
        # Obtém a semente aleatória do serviço Random.org
        seed = obter_bytes_aleatorios()
    
    random.seed(seed)
    
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
        try:
            seed = int(input("Digite a semente aleatória (deixe em branco para aleatoriedade padrão): "))
        except ValueError:
            seed = None

        grupos = gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero, seed)
        imprimir_grupos(grupos)
        exit()

    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    #coletar_valores_entrada()
    n_grupos = 5  # Altere o número de grupos conforme necessário
    n_numeros_por_grupo = 6
    min_numero = 1
    max_numero = 60
    seed = None # '625EZpEUy8dx2K@$#@$S2YtqfT968' # Torna os resultados reproduzíveis (sempre iguais)

    grupos = gerar_grupos(n_grupos, n_numeros_por_grupo, min_numero, max_numero, seed)

    imprimir_grupos(grupos)