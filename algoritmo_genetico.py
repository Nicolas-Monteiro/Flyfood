import numpy as np
import random
import math

def custoCaminho(permutacao, matriz_custos, mapa_indice):
    
    soma = 0
    R_indice = mapa_indice['R']
    
    primeiro_ponto_nome = permutacao[0]
    v1_indice = mapa_indice[primeiro_ponto_nome]
    soma += matriz_custos[R_indice, v1_indice]
    
    for i in range(len(permutacao) - 1):
        a_nome = permutacao[i]
        b_nome = permutacao[i+1]
        a_indice = mapa_indice[a_nome]
        b_indice = mapa_indice[b_nome]
        soma += matriz_custos[a_indice, b_indice]
            
    ultimo_ponto_nome = permutacao[-1]
    vN_indice = mapa_indice[ultimo_ponto_nome]
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

def processar_matriz_de_custos(dados_custos, nomes_pontos):
    
    #Validação
    num_pontos_esperado = len(nomes_pontos)
    if num_pontos_esperado != len(dados_custos):
        raise ValueError("O número de nomes de pontos não corresponde ao tamanho da matriz.")
        
    matriz_custos = np.array(dados_custos, dtype=int)
    mapa_indice = {nome: i for i, nome in enumerate(nomes_pontos)}
    pontos_interesse = nomes_pontos[1:]
    
    return matriz_custos, pontos_interesse, mapa_indice

def inicializar_populacao(tamanho_populacao, pontos_interesse):
    
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = pontos_interesse[:]
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao


def iniciar_algoritmo_genetico(tamanho_populacao):
   
    NOMES_PONTOS = ['R', 'A', 'B', 'C', 'D']
    DADOS_CUSTOS = [
        [0, 3, 2, 5, 7],
        [3, 0, 3, 4, 4],
        [2, 3, 0, 3, 5],
        [5, 4, 3, 0, 2],
        [7, 4, 5, 2, 0]
    ]
    
    MATRIZ_CUSTOS, PONTOS_INTERESSE, MAPA_INDICE = processar_matriz_de_custos(
        DADOS_CUSTOS, NOMES_PONTOS
    )
    
    populacao_inicial = inicializar_populacao(tamanho_populacao, PONTOS_INTERESSE)
    
    lista_aptidao, lista_custos = calculaAptidao(
        populacao_inicial, MATRIZ_CUSTOS, MAPA_INDICE
    )
    
    
    melhor_aptidao_indice = np.argmax(lista_aptidao)
    melhor_custo = lista_custos[melhor_aptidao_indice]
    melhor_rota = populacao_inicial[melhor_aptidao_indice]

    print("Matriz de Custos Recebida:")
    print(MATRIZ_CUSTOS)
    print("-" * 30)
    print(f"Total de Pontos a Visitar: {len(PONTOS_INTERESSE)}")
    print(f"Mapa de Tradução (Nome -> Índice): {MAPA_INDICE}")
    print("-" * 30)
    print(f"População Inicial (Tamanho: {tamanho_populacao}) com Aptidão:")
    
    # Exibir cada rota com seu custo e aptidão
    for i in range(tamanho_populacao):
        is_melhor = " <--- MELHOR ROTA " if i == melhor_aptidao_indice else ""
        print(
            f"Rota {i+1}: {populacao_inicial[i]} | Custo: {lista_custos[i]:.2f} | Aptidão: {lista_aptidao[i]:.4f}{is_melhor}"
        )

    print("-" * 30)
    print(f"Melhor Rota  : {['R'] + melhor_rota + ['R']}")
    print(f"Custo Mínimo : {melhor_custo:.2f}")

if __name__ == "__main__":
  
    iniciar_algoritmo_genetico(tamanho_populacao=50)