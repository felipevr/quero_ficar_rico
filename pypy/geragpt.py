import random
import itertools

def gerar_jogos(qtd_jogos: int, tipo: str, dezenas_por_jogo: int = None,
                fixos=None, excluidos=None, seed=None):
    """
    Gera jogos de loteria com cobertura máxima e mínima repetição.
    
    Parâmetros:
        qtd_jogos (int): Quantidade de bilhetes/jogos a gerar.
        tipo (str): Tipo de jogo: 'megasena', 'quina' ou 'lotofacil'.
        dezenas_por_jogo (int): Quantidade de dezenas por bilhete (se None, usa o mínimo padrão).
        fixos (list[int]): Números fixos que sempre entram em todos os jogos.
        excluidos (list[int]): Números que nunca entram nos jogos.
        seed (int): Valor para fixar a aleatoriedade (opcional).
    
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

    if seed is not None:
        random.seed(seed)

    fixos = set(fixos or [])
    excluidos = set(excluidos or [])

    if not fixos.issubset(set(range(1, total_dezenas + 1))):
        raise ValueError("Algum número fixo é inválido!")
    if not excluidos.issubset(set(range(1, total_dezenas + 1))):
        raise ValueError("Algum número excluído é inválido!")

    # Inicializa todos os números possíveis (já removendo os excluídos e fixos serão tratados depois)
    numeros_possiveis = [n for n in range(1, total_dezenas + 1) if n not in excluidos]

    # Contador de uso das dezenas (para balancear a cobertura)
    contador = {n: 0 for n in numeros_possiveis}

    jogos = []
    for _ in range(qtd_jogos):
        candidatos = sorted(numeros_possiveis, key=lambda x: (contador[x], random.random()))
        
        # Quantos ainda faltam além dos fixos
        faltam = dezenas_por_jogo - len(fixos)
        if faltam < 0:
            raise ValueError("Quantidade de fixos maior que a quantidade de dezenas por jogo.")

        jogo = sorted(list(fixos) + candidatos[:faltam])
        
        for n in jogo:
            if n in contador:  # fixos podem não estar no contador se eram excluídos
                contador[n] += 1
        jogos.append(jogo)

    return jogos


def is_subset_game(game_a, game_b):
    """Retorna True se todos os números de `game_a` estiverem em `game_b`."""
    return set(game_a).issubset(set(game_b))


def find_redundant_games(jogos):
    """Retorna a lista de índices de jogos que estão totalmente contidos em outro jogo.

    Um jogo A é considerado redundante se existe algum jogo B (B != A) tal que A ⊆ B.
    """
    sets = [set(j) for j in jogos]
    redundant = set()
    n = len(sets)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if sets[i].issubset(sets[j]):
                redundant.add(i)
                break
    return sorted(list(redundant))


def remove_redundant_games(jogos):
    """Retorna uma nova lista de jogos sem os que são redundantes (conteúdo em outro jogo)."""
    red = set(find_redundant_games(jogos))
    return [j for idx, j in enumerate(jogos) if idx not in red]


def combinations_covered(jogos, k=6):
    """Retorna o conjunto de combinações distintas de tamanho `k` cobertas pelos jogos.

    Observação: para jogos muito grandes ou muitos jogos, isso pode consumir memória.
    """
    combos = set()
    for jogo in jogos:
        if len(jogo) < k:
            continue
        for comb in itertools.combinations(sorted(jogo), k):
            combos.add(tuple(comb))
    return combos


def coverage_stats(jogos, k=6):
    """Retorna o número de combinações distintas de tamanho `k` cobertas pelos jogos."""
    return len(combinations_covered(jogos, k))


if __name__ == "__main__":
    # Exemplo de uso e verificação
    jogos = gerar_jogos(15, "megasena", dezenas_por_jogo=10, fixos=[7, 13], excluidos=[60], seed=42)

    # Adiciona alguns jogos de demonstração (um é subconjunto de outro)
    demo = [
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],  # contém o anterior
        [10, 11, 12, 13, 14, 15, 16],
        [20, 21, 22, 23, 24, 25, 26, 27],
    ]
    jogos_all = jogos + demo

    redundant = find_redundant_games(jogos_all)
    print("Jogos gerados (total):", len(jogos_all))
    print("Indices redundantes (conteúdo em outro jogo):", redundant)
    print("Jogos sem redundância:")
    for j in remove_redundant_games(jogos_all):
        print(sorted(j))
    print("Cobertura de combinações de 6 dezenas (únicas):", coverage_stats(jogos_all, 6))
