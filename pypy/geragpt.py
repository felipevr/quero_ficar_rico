import random

def gerar_jogos(qtd_jogos: int, tipo: str, dezenas_por_jogo: int = None):
    """
    Gera jogos de loteria com cobertura máxima e mínima repetição.
    
    Parâmetros:
        qtd_jogos (int): Quantidade de bilhetes/jogos a gerar.
        tipo (str): Tipo de jogo: 'megasena', 'quina' ou 'lotofacil'.
        dezenas_por_jogo (int): Quantidade de dezenas por bilhete (se None, usa o mínimo padrão).
    
    Retorno:
        list[list[int]]: Lista de jogos gerados.
    """

    # Configuração dos jogos
    configuracoes = {
        "megasena": {"min": 6, "max": 20, "total": 60},
        "quina": {"min": 5, "max": 15, "total": 80},
        "lotofacil": {"min": 15, "max": 20, "total": 25}
    }
    
    if tipo not in configuracoes:
        raise ValueError("Tipo de jogo inválido! Use: 'megasena', 'quina' ou 'lotofacil'.")

    minimo = configuracoes[tipo]["min"]
    maximo = configuracoes[tipo]["max"]
    total_dezenas = configuracoes[tipo]["total"]

    if dezenas_por_jogo is None:
        dezenas_por_jogo = minimo
    elif dezenas_por_jogo < minimo or dezenas_por_jogo > maximo:
        raise ValueError(f"Quantidade de dezenas deve estar entre {minimo} e {maximo}.")

    # Inicializa todos os números possíveis
    numeros_possiveis = list(range(1, total_dezenas + 1))

    # Contador de uso das dezenas (para balancear a cobertura)
    contador = {n: 0 for n in numeros_possiveis}

    jogos = []
    for _ in range(qtd_jogos):
        # Ordena os números pelo menor uso (para dar cobertura máxima)
        candidatos = sorted(numeros_possiveis, key=lambda x: (contador[x], random.random()))
        # Seleciona os menos usados
        jogo = sorted(candidatos[:dezenas_por_jogo])
        # Marca como usados
        for n in jogo:
            contador[n] += 1
        jogos.append(jogo)

    return jogos


# Exemplo de uso
if __name__ == "__main__":
    print("Mega-Sena:")
    for jogo in gerar_jogos(5, "megasena"):
        print(jogo)

    print("\nQuina:")
    for jogo in gerar_jogos(5, "quina"):
        print(jogo)

    print("\nLotofácil:")
    for jogo in gerar_jogos(3, "lotofacil", dezenas_por_jogo=18):
        print(jogo)
