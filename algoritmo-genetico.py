import numpy as np
import random
import os

# FUNÇÕES DE CUSTO E APTIDÃO 

def custoCaminho(permutacao, matriz_custos, mapa_indice):
    soma = 0

    R_indice = mapa_indice[0]
    
    v1_indice = mapa_indice[permutacao[0]]
    soma += matriz_custos[R_indice, v1_indice]
    
    for i in range(len(permutacao) - 1):
        a_indice = mapa_indice[permutacao[i]]
        b_indice = mapa_indice[permutacao[i+1]]
        soma += matriz_custos[a_indice, b_indice]
            
    vN_indice = mapa_indice[permutacao[-1]]
    soma += matriz_custos[vN_indice, R_indice]
        
    return soma

def calculaAptidao(populacao, matriz_custos, mapa_indice):
    listaAptidao = []
    listaCustos = []
    
    for individuo in populacao:
        custo = custoCaminho(individuo, matriz_custos, mapa_indice)
        listaCustos.append(custo)
        
        aptidao = 1 / custo
        listaAptidao.append(aptidao)
        
    return listaAptidao, listaCustos

# FUNÇÃO DE PROCESSAMENTO DA MATRIZ MODIFICADA

def processar_matriz_de_custos(matriz_entrada, num_total_pontos):
    
    NOMES_PONTOS = list(range(num_total_pontos)) 
    NUM_TOTAL_PONTOS = num_total_pontos
    
    elementos_str = matriz_entrada.replace('\n', ' ').replace('\t', ' ').split()
    
    try:
        pesos = [int(p) for p in elementos_str]
    except ValueError:
        raise ValueError("ERRO: O arquivo de custos contém caracteres não numéricos.")

    matriz_custos = np.zeros((NUM_TOTAL_PONTOS, NUM_TOTAL_PONTOS), dtype=int)
    
    mapa_indice = {nome: i for i, nome in enumerate(NOMES_PONTOS)}
    
    peso_indice = 0
    
    for i in range(NUM_TOTAL_PONTOS):
        for j in range(i + 1, NUM_TOTAL_PONTOS):
            
            if peso_indice >= len(pesos):
                
                num_pesos_esperados = NUM_TOTAL_PONTOS * (NUM_TOTAL_PONTOS - 1) // 2
                raise ValueError(
                    f"ERRO: O arquivo tem {len(pesos)} custos. O número de pontos ({NUM_TOTAL_PONTOS}) exige {num_pesos_esperados} custos."
                )
            
            peso = pesos[peso_indice]
            
            matriz_custos[i, j] = peso
            matriz_custos[j, i] = peso
            
            peso_indice += 1
            
    pontos_interesse = NOMES_PONTOS[1:] 
    
    return matriz_custos, pontos_interesse, mapa_indice

# INICIALIZAR POPULAÇÃO 

def inicializar_populacao(tamanho_populacao, pontos_interesse):
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = pontos_interesse[:]
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao

# FUNÇÃO DE EXECUÇÃO MODIFICADA

def executar(tamanho_populacao):
    
    NOME_ARQUIVO = "teste.txt"
    STRING_CUSTOS = ""
    NUM_LINHAS = 0

    try:
        if not os.path.exists(NOME_ARQUIVO):
            raise FileNotFoundError(f"O arquivo '{NOME_ARQUIVO}' não foi encontrado.")
            
        with open(NOME_ARQUIVO, "r") as arquivo:
            linhas = arquivo.readlines()
            STRING_CUSTOS = "".join(linhas)
            
            NUM_LINHAS = sum(1 for linha in linhas if linha.strip())
            
        NUM_TOTAL_PONTOS = NUM_LINHAS + 1
        
        if NUM_TOTAL_PONTOS < 2:
            print("=" * 65)
            print("ERRO: O arquivo deve conter pelo menos 1 linha de custos (para 2 pontos no total: 0 e 1).")
            print("=" * 65)
            return

    except FileNotFoundError as e:
        print("=" * 65)
        print(f"ERRO DE ARQUIVO: {e}")
        print("=" * 65)
        return
    except Exception as e:
        print("=" * 65)
        print(f"ERRO INESPERADO ao abrir/ler o arquivo: {e}")
        print("=" * 65)
        return
    
    try:
        MATRIZ_CUSTOS, PONTOS_INTERESSE, MAPA_INDICE = processar_matriz_de_custos(
            STRING_CUSTOS, NUM_TOTAL_PONTOS 
        )
    except ValueError as e:
        print("=" * 65)
        print(f"ERRO NO PROCESSAMENTO DOS DADOS: {e}")
        print("Verifique se o conteúdo do arquivo 'teste.txt' tem a quantidade correta de custos.")
        print("=" * 65)
        return 
    
    populacao_inicial = inicializar_populacao(tamanho_populacao, PONTOS_INTERESSE)
    
    lista_aptidao, lista_custos = calculaAptidao(
        populacao_inicial, MATRIZ_CUSTOS, MAPA_INDICE
    )
    
    melhor_aptidao_indice = np.argmax(lista_aptidao)
    melhor_custo = lista_custos[melhor_aptidao_indice]
    melhor_rota = populacao_inicial[melhor_aptidao_indice]

    
    print("Matriz de Custos:")
    print(MATRIZ_CUSTOS)
    print("-" * 65)
    print(f"Mapa de Tradução (Ponto -> Índice da Matriz): {MAPA_INDICE}")
    print(f"Total de Pontos (N): {NUM_TOTAL_PONTOS} (Ponto de Retorno: 0, Pontos de Interesse: {PONTOS_INTERESSE})")
    print("-" * 65)
    
    print(f"População Inicial (Tamanho: {tamanho_populacao}):")
    
    for i in range(tamanho_populacao):
        is_melhor = " <-- MELHOR ROTA" if i == melhor_aptidao_indice else ""
        
        rota_str = ' -> '.join(map(str, populacao_inicial[i]))
        
        print(
            f"Rota {i+1}: {populacao_inicial[i]} | Custo: {lista_custos[i]:.2f} | Aptidão: {lista_aptidao[i]:.4f}{is_melhor}"
        )

    print("-" * 65)
  
    melhor_rota_str = ' -> '.join(map(str, melhor_rota))
    print(f"Melhor Rota : 0 -> {melhor_rota_str} -> 0")
    print(f"Custo Mínimo: {melhor_custo:.2f}")
    print("===============================================================")

# CHAMADA DO PROGRAMA 
if __name__ == "__main__":
    executar(15)
