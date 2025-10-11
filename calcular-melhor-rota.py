def gerar_permutacoes(elementos):
    #Recursivamente gerar todas as permutações possíveis de uma lista de elementos
    if len(elementos) == 0:
        return [[]]
    
    todas_permutacoes = []
    for i in range(len(elementos)):
        elemento_atual = elementos[i]
        elementos_restantes = elementos[:i] + elementos[i+1:]
        
        for permutacao in gerar_permutacoes(elementos_restantes):
            todas_permutacoes.append([elemento_atual] + permutacao)
            
    return todas_permutacoes

def calcular_distancia(ponto1, ponto2):
    #Calcular a distância de Manhattan entre dois pontos (tuplas de coordenadas)
    
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

def calcular_caminhos(matriz):
    #Calcular o caminho mais curto que visita todos os pontos de interesse e retorna ao ponto de partida
    
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    pontos_interesse = {}
    ponto_partida = None

    for l in range(num_linhas):
        for c in range(num_colunas):
            elemento = matriz[l][c]
            if elemento == 'R':
                ponto_partida = (l, c)
            elif elemento.isalpha() and elemento != '0':
                pontos_interesse[elemento] = (l, c)
    
    if not ponto_partida or not pontos_interesse:
        return None, None, "Erro: 'R' ou pontos de interesse não encontrados."

    pontos_a_visitar = sorted(list(pontos_interesse.keys()))
    
    menor_distancia = float('inf')
    melhor_caminho = []

    todas_rotas = gerar_permutacoes(pontos_a_visitar)

    print("INICIO\n")

    for i, permutacao_pontos in enumerate(todas_rotas):
        distancia_atual = 0
        caminho_atual_exibicao = ['R']
        
        ponto_anterior_coord = ponto_partida
        
        for ponto_nome in permutacao_pontos:
            ponto_atual_coord = pontos_interesse[ponto_nome]
            distancia_segmento = calcular_distancia(ponto_anterior_coord, ponto_atual_coord)
            distancia_atual += distancia_segmento
            caminho_atual_exibicao.append(ponto_nome)
            ponto_anterior_coord = ponto_atual_coord

        ultimo_ponto_coord = pontos_interesse[permutacao_pontos[-1]]
        distancia_volta = calcular_distancia(ultimo_ponto_coord, ponto_partida)
        distancia_atual += distancia_volta
        caminho_atual_exibicao.append('R')
        
        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_caminho = caminho_atual_exibicao
            
            print(f"Rota {i+1} é a nova melhor!")
            print(f"Caminho: {' -> '.join(melhor_caminho)} - Distância: {menor_distancia}\n")
            
    print("FIM")
    return menor_distancia, melhor_caminho, None

def processar_entrada(string_entrada):
    # Processar a string de entrada para extrair a matriz e validar dimensões
    
    linhas = string_entrada.strip().split('\n')
    try:
        dimensoes = list(map(int, linhas[0].split()))
        linhas_esperadas, colunas_esperadas = dimensoes[0], dimensoes[1]
    except (ValueError, IndexError):
        return None, "Erro: A primeira linha deve conter as dimensões 'linhas colunas' (Ex: 4 5)."

    matriz = []
    if len(linhas) - 1 != linhas_esperadas:
        return None, f"Erro: A matriz tem {len(linhas) - 1} linhas, mas o esperado era {linhas_esperadas}."

    for i in range(1, len(linhas)):
        elementos_linha = linhas[i].split()
        if len(elementos_linha) != colunas_esperadas:
            return None, f"Erro: A linha {i} tem {len(elementos_linha)} colunas, mas o esperado era {colunas_esperadas}."
        matriz.append(elementos_linha)
    
    return matriz, None

# --- Uso do Código ---
string_entrada_exemplo = """
4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0

"""

matriz_dados, mensagem_erro = processar_entrada(string_entrada_exemplo)

if matriz_dados:
    distancia_minima, melhor_rota, erro= calcular_caminhos(matriz_dados)
    
    if erro:
        print(erro)
    elif distancia_minima is not None:
        print("="*30)
        print(f"RESULTADO FINAL:")
        print(f"Menor Distância Total: {distancia_minima}")
        print(f"Melhor Rota: {' -> '.join(melhor_rota)}")
        print("="*30)
else:
    print(mensagem_erro)
