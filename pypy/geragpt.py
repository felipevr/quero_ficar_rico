import random


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


# Exemplo de uso
if __name__ == "__main__":
    print("Mega-Sena:")
    for jogo in gerar_jogos(5, "megasena", fixos=[60], excluidos=[7, 13], seed=123):
        print(jogo)

    print("\nQuina:")
    for jogo in gerar_jogos(5, "quina"):
        print(jogo)

    print("\nLotofácil:")
    for jogo in gerar_jogos(3, "lotofacil", dezenas_por_jogo=18, excluidos=[13], seed=42):
        print(jogo)
