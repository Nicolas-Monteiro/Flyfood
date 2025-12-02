# FlyFood: Otimizador de Rotas 🛸

Este projeto é uma implementação em Python para solucionar o Problema do Caixeiro Viajante (PCV) aplicado à logística de entregas de drones. O sistema foi desenvolvido em duas etapas, oferecendo **duas abordagens distintas** de resolução:

1.  **Força Bruta (Exact Solver):** Garante a rota matematicamente ótima testando todas as permutações ($O(N!)$). Ideal para validação e pequenas instâncias ($N \le 12$).
2.  **Algoritmo Genético (Heuristic Solver):** Utiliza conceitos evolutivos (Seleção, Crossover e Mutação) para encontrar rotas eficientes em instâncias de grande escala ($N > 12$) e benchmarks como a TSPLIB (ex: `brazil58`), onde a força bruta seria inviável.

## ✨ Funcionalidades

Este repositório contém 4 scripts principais, divididos entre métodos de resolução e ferramentas de análise visual:

* **`calcular-melhor-rota.py`:** Implementação da **Força Bruta**. Recebe uma matriz de pontos, calcula todas as permutações possíveis e retorna a distância mínima global.
* **`algoritmo_genetico.py`:** Implementação da **Meta-heurística**. Utiliza Crossover Ordenado e Mutação por Inversão para resolver matrizes grandes ou arquivos `.tsp` (TSPLIB) em segundos.
* **`grafico-processamento.py`:** Um script visual que plota as coordenadas e desenha a melhor rota encontrada em um gráfico 2D, facilitando a interpretação do trajeto.
* **`grafico-complexidade.py`:** Um script educacional que gera um gráfico comparativo entre as complexidades Fatorial $O(N!)$, Quadrática $O(N^2)$ e Linear $O(N)$, ilustrando o limite operacional dos métodos exatos.

   ## ⚙️ Instalação e Configuração

Siga os passos abaixo para preparar o ambiente e rodar o projeto.

### Pré-requisitos

-   Python 3.x instalado em seu sistema.

### Passos

1.  **Clone o repositório** (ou baixe os arquivos para uma pasta em seu computador).
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Instale as dependências.** Os scripts de visualização precisam das bibliotecas `matplotlib` e `numpy`. Instale-as usando o pip (essas bibliotecas so são usadas para visualização dos gráficos):
    ```bash
    pip install matplotlib numpy
    ```
    * `numpy`: Usada para cálculos matemáticos eficientes com matrizes.
    * `matplotlib`: Usada para gerar os gráficos.

## 🚀 Como Executar

Cada funcionalidade pode ser executada de forma independente através do terminal. Certifique-se de que seu terminal esteja aberto na pasta do projeto.

---

### 1. Encontrar a melhor rota para o drone ( força bruta )

▶️ **Para executar, use o comando:**
```bash
python calcular-melhor-rota.py
```
Saída esperada: O terminal irá imprimir a sequência ótima dos pontos e a distância total da rota.

Nota: Para alterar os pontos de entrega, você precisará editar a matriz de coordenadas diretamente dentro do arquivo calcular-melhor-rota.py.

### 2. Encontrar a melhor rota para o drone ( Heurística )
```bash
python algoritimo-genetico.py
```
Saída esperada: O terminal irá imprimir a sequência ótima dos pontos e o custo total da rota.

Nota: Para alterar os pontos de entrega, você precisará editar a entrada do código para o nome do arquivo de teste desejado

### 3. Visualizar o gráfico de tempo de processamento do algoritmo

▶️ **Para executar, use o comando:**
```bash
python grafico-processamento.py
```
Saída esperada: Uma janela se abrirá mostrando o gráfico do tempo de processamento do problema em questão

### 4. Visualizar o gráfico de complexidade 

▶️ **Para executar, use o comando:**
```bash
python calcular-melhor-rota.py
```
Saída esperada: Uma janela se abrirá com o gráfico comparando o crescimento das complexidades $O(N)$, $O(N^2)$ e $O(N!)$.

## 🤝 Colaboradores
- **Edmir Nicácio Lopes Neto** - (https://github.com/nicacionetodev)

## 📚 Artigo de Referência

Este projeto foi desenvolvido com base nos conceitos e resultados apresentados no seguinte artigo. Para uma análise mais aprofundada da metodologia e dos resultados de desempenho, consulte:

- **link para o artigo: (https://docs.google.com/document/d/e/2PACX-1vT4y6TJ7Mm4mpAbd8THa6-DRw4kUK4RremPxzbkchx1JhY1dZ3CpjXAP5NG9nOjdcnF-jV1xWgwMLNa/pub)**
  - *Autores: Nícolas Matheus Gonzaga Monteiro e Edmir Nicácio Lopes Neto*

.
