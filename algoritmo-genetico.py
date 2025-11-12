import numpy as np
import random

#FUNÇÕES DE CUSTO E APTIDÃO 

def custoCaminho(permutacao, matriz_custos, mapa_indice):
    soma = 0
    R_indice = mapa_indice['R']
    
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

#FUNÇÃO DE PROCESSAMENTO DA MATRIZ

def processar_matriz_de_custos(matriz_entrada):
    
    NOMES_PONTOS = ['R', 'A', 'B', 'C', 'D']
    NUM_TOTAL_PONTOS = len(NOMES_PONTOS)
    
    elementos_str = matriz_entrada.replace('\n', ' ').replace('\t', ' ').split()
    
    try:
        pesos = [int(p) for p in elementos_str]
    except ValueError:
        raise ValueError("ERRO: A string de custos contém caracteres não numéricos.")

    matriz_custos = np.zeros((NUM_TOTAL_PONTOS, NUM_TOTAL_PONTOS), dtype=int)
    mapa_indice = {nome: i for i, nome in enumerate(NOMES_PONTOS)}
    
    peso_indice = 0
    
    for i in range(NUM_TOTAL_PONTOS):
        for j in range(i + 1, NUM_TOTAL_PONTOS):
            
            if peso_indice >= len(pesos):
                raise ValueError("ERRO: A string não possui o número suficiente de custos.")
            
            peso = pesos[peso_indice]
            
            matriz_custos[i, j] = peso
            matriz_custos[j, i] = peso
            
            peso_indice += 1
            
    pontos_interesse = NOMES_PONTOS[1:]
    
    # LINHA ESSENCIAL QUE ESTAVA FALTANDO:
    return matriz_custos, pontos_interesse, mapa_indice

#INICIALIZAR POPULAÇÃO

def inicializar_populacao(tamanho_populacao, pontos_interesse):
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = pontos_interesse[:]
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao

#FUNÇÃO DE EXECUÇÃO

def executar(tamanho_populacao):
    
    STRING_CUSTOS = """
    3 2 5 7
    3 4 4
    3 5
    2
    """

    try:
        MATRIZ_CUSTOS, PONTOS_INTERESSE, MAPA_INDICE = processar_matriz_de_custos(
            STRING_CUSTOS
        )
    except ValueError as e:
        print("=" * 65)
        print(f"ERRO NO PROCESSAMENTO DOS DADOS: {e}")
        print("Verifique se a string de custos está completa.")
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
    print(f"Mapa de Tradução: {MAPA_INDICE}")
    print("-" * 65)
    
    print(f"População Inicial (Tamanho: {tamanho_populacao}):")
    
    for i in range(tamanho_populacao):
        is_melhor = " <-- MELHOR ROTA" if i == melhor_aptidao_indice else ""
        print(
            f"Rota {i+1}: {populacao_inicial[i]} | Custo: {lista_custos[i]:.2f} | Aptidão: {lista_aptidao[i]:.4f}{is_melhor}"
        )

    print("-" * 65)
    print(f"Melhor Rota : R -> {' -> '.join(melhor_rota)} -> R")
    print(f"Custo Mínimo: {melhor_custo:.2f}")
    print("===============================================================")

# --- CHAMADA DO PROGRAMA ---
if __name__ == "__main__":
    executar(15)