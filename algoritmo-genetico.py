import numpy as np
import random
import re

# FUNÇÕES DE CUSTO E APTIDÃO 

def custo_caminho(permutacao, dic_distancias):
    soma = 0
    
    for i in range(len(permutacao) - 1):
        a = permutacao[i]
        b = permutacao[i+1]
        if (a, b) in dic_distancias:
            soma += dic_distancias[(a, b)]
        else:
            raise ValueError(f"Caminho não encontrado no dicionário: ({a},{b})")
            
    ultimo_no = permutacao[-1]
    primeiro_no = permutacao[0]
    
    if (ultimo_no, primeiro_no) in dic_distancias:
        soma += dic_distancias[(ultimo_no, primeiro_no)]
    else:
        raise ValueError(f"Caminho de retorno não encontrado: ({ultimo_no},{primeiro_no})")
        
    return soma

def calcula_aptidao(populacao, dic_distancias):
    listaAptidao = []
    listaCustos = []
    
    for individuo in populacao:
        custo = custo_caminho(individuo, dic_distancias)
        listaCustos.append(custo)
        
        aptidao = 1 / custo if custo > 0 else 0
        listaAptidao.append(aptidao)
        
    return listaAptidao, listaCustos

# FUNÇÃO DE PROCESSAMENTO DE ENTRADA 

def processar_entrada(caminho_arquivo):
    
    try:
        with open(caminho_arquivo, 'r') as objArq:
            conteudo = objArq.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"ERRO: Arquivo não encontrado no caminho: '{caminho_arquivo}'")

    limpo = re.sub(r'\s+', ' ', conteudo).strip()
    elementos_str = limpo.split()
    
    try:
        pesos = [int(p) for p in elementos_str]
    except ValueError:
        raise ValueError(f"ERRO: O arquivo {caminho_arquivo} contém dados não numéricos.")

    total_de_custos_fornecidos = len(pesos)
    
    NUM_TOTAL_PONTOS = 0
    while NUM_TOTAL_PONTOS * (NUM_TOTAL_PONTOS - 1) / 2 < total_de_custos_fornecidos:
        NUM_TOTAL_PONTOS += 1
    
    if NUM_TOTAL_PONTOS * (NUM_TOTAL_PONTOS - 1) / 2 != total_de_custos_fornecidos:
        raise ValueError(f"ERRO: O número de custos fornecidos ({total_de_custos_fornecidos}) não corresponde a uma matriz triangular válida.")
    
    dic_distancias = {}
    peso_indice = 0
    
    for i in range(1, NUM_TOTAL_PONTOS):
        for j in range(i + 1, NUM_TOTAL_PONTOS + 1): 
            
            peso = pesos[peso_indice]
            
            dic_distancias[(i, j)] = peso
            dic_distancias[(j, i)] = peso
            
            peso_indice += 1
            
    return dic_distancias, NUM_TOTAL_PONTOS

# --- INICIALIZAR POPULAÇÃO (CORRIGIDO) ---

def inicializar_populacao(tamanho_populacao, qtde_cidades):
    populacao = []
    
    cidades_base = list(range(1, qtde_cidades + 1)) 
    
    for _ in range(tamanho_populacao):
       
        individuo = cidades_base[:]
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao

# SELEÇÃO 

def selecao_torneio(populacao, lista_aptidao, tamanho_torneio=5):
   
    melhor_indice = -1
    melhor_aptidao = -1.0
    
    tamanho_populacao = len(populacao)
    participantes_indices = random.sample(range(tamanho_populacao), tamanho_torneio)
    
    for indice in participantes_indices:
        aptidao_atual = lista_aptidao[indice]
        
        if aptidao_atual > melhor_aptidao:
            melhor_aptidao = aptidao_atual
            melhor_indice = indice
            
    return populacao[melhor_indice]

# CROSSOVER

def crossover(pai1, pai2):
   
    tamanho = len(pai1)
    
    ponto_corte1 = random.randint(0, tamanho - 1)
    ponto_corte2 = random.randint(0, tamanho - 1)
    
    if ponto_corte1 > ponto_corte2:
        ponto_corte1, ponto_corte2 = ponto_corte2, ponto_corte1
        
    filho = [None] * tamanho
    segmento_pai1 = pai1[ponto_corte1:ponto_corte2 + 1]
    filho[ponto_corte1:ponto_corte2 + 1] = segmento_pai1
    
    genes_presentes = set(segmento_pai1)
    p2_index = ponto_corte2 + 1
    f_index = ponto_corte2 + 1
    
    for _ in range(tamanho):
        
        if p2_index >= tamanho: p2_index = 0
        if f_index >= tamanho: f_index = 0
            
        gene_pai2 = pai2[p2_index]
        
        if filho[f_index] is None:
            if gene_pai2 not in genes_presentes:
                filho[f_index] = gene_pai2
                f_index += 1
                
        p2_index += 1
            
    return filho

# MUTAÇÃO

def mutacao(individuo, taxa_mutacao=0.05):
    
    if random.random() < taxa_mutacao:
        tamanho = len(individuo)
        
        ponto_corte1 = random.randint(0, tamanho - 1)
        ponto_corte2 = random.randint(0, tamanho - 1)
        
        if ponto_corte1 > ponto_corte2:
            ponto_corte1, ponto_corte2 = ponto_corte2, ponto_corte1
        
        segmento_a_inverter = individuo[ponto_corte1 : ponto_corte2 + 1]
        segmento_invertido = segmento_a_inverter[::-1] 
        
        individuo[ponto_corte1 : ponto_corte2 + 1] = segmento_invertido
        
    return individuo
 
# ALGORITMO GENÉTICO

def algoritmo_genetico(dic_distancias, qtde_cidades, parametros):
    
    TAMANHO_POP = parametros['tamanho_populacao']
    MAX_GERACOES = parametros['max_geracoes']
    TAXA_CROSSOVER = parametros['taxa_crossover']
    TAXA_MUTACAO = parametros['taxa_mutacao']
    TAM_TORNEIO = parametros['tamanho_torneio']
    
    populacao_atual = inicializar_populacao(TAMANHO_POP, qtde_cidades)
    
    melhor_custo_global = float('inf')
    melhor_rota_global = []
    
    for geracao in range(MAX_GERACOES):
        
        lista_aptidao_atual, lista_custos_atual = calcula_aptidao(populacao_atual, dic_distancias)
        
        indice_melhor_atual = np.argmin(lista_custos_atual) 
        custo_melhor_atual = lista_custos_atual[indice_melhor_atual]
        rota_melhor_atual = populacao_atual[indice_melhor_atual]
        
        if custo_melhor_atual < melhor_custo_global:
            melhor_custo_global = custo_melhor_atual
            melhor_rota_global = rota_melhor_atual[:]
            print(f"Geração {geracao}: Novo Melhor Custo -> {melhor_custo_global:.2f}")
    
        nova_populacao = [melhor_rota_global[:]] 
        
        while len(nova_populacao) < TAMANHO_POP:
            
            pai1 = selecao_torneio(populacao_atual, lista_aptidao_atual, TAM_TORNEIO)
            pai2 = selecao_torneio(populacao_atual, lista_aptidao_atual, TAM_TORNEIO)
            
            if random.random() < TAXA_CROSSOVER:
                filho = crossover(pai1, pai2)
            else:
                filho = pai1[:] 

            filho = mutacao(filho, TAXA_MUTACAO)
            
            nova_populacao.append(filho)
            
        populacao_atual = nova_populacao
        
    return melhor_rota_global, melhor_custo_global

# FUNÇÃO DE EXECUÇÃO  

def executar(caminho_arquivo):
    
    PARAMETROS_AG = {
        'tamanho_populacao': 200,
        'max_geracoes': 1000,
        'taxa_crossover': 0.9,
        'taxa_mutacao': 0.1, 
        'tamanho_torneio': 4
    }
    
    try:
        dic_distancias, qtde_cidades = processar_entrada(caminho_arquivo)
    except (ValueError, FileNotFoundError) as e:
        print(f"ERRO DE LEITURA/PROCESSAMENTO: {e}")
       
        return 
    tempo_inicio = time.time()
    melhor_rota, melhor_custo = algoritmo_genetico(dic_distancias, qtde_cidades, PARAMETROS_AG)
    tempo_total = time.time() - tempo_inicio
    
    print(f"RESULTADO FINAL DO ALGORITMO GENÉTICO (N={qtde_cidades})\n")
    print(f"Melhor Custo Encontrado: {melhor_custo:.2f}")
    print(f"Melhor Rota (Início -> Fim): {melhor_rota}")
    print(f"Tempo de Execução Total: {tempo_total:.4f} segundos")

if __name__ == "__main__":

    executar("teste_brasil58.txt")

if __name__ == "__main__":

    executar("teste_brasil58.txt")
