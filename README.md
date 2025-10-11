# FlyFood: Otimizador de Rotas 🛸

Este projeto é uma implementação em Python para solucionar o Problema do Caixeiro Viajante (PCV) utilizando uma abordagem de força bruta. Ele calcula a rota mais curta que passa por um conjunto de pontos e retorna à origem.

Além do cálculo principal, o projeto inclui scripts para visualizar a rota ótima em um gráfico e para gerar uma análise visual da complexidade computacional do algoritmo.

## ✨ Funcionalidades

Este repositório contém 3 funcionalidades principais, cada uma em seu próprio arquivo:

1.  **`calcular-melhor-rota.py`**: O script principal que recebe uma matriz de pontos e calcula a rota mais curta possível, imprimindo o resultado no terminal.
2.  **`grafico-processamento.py`**: Um script visual que plota os pontos e a melhor rota encontrada em um gráfico 2D, ajudando a entender o resultado.
3.  **`grafico-complexidade.py`**: Um script educacional que gera um gráfico comparando a complexidade Fatorial `$O(N!)$` (usada neste projeto) com outras complexidades (Linear e Quadrática) para ilustrar por que a força bruta é inviável para muitos pontos.

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

### 1. Encontrar a melhor rota para o drone

▶️ **Para executar, use o comando:**
```bash
python calcular-melhor-rota.py
```
Saída esperada: O terminal irá imprimir a sequência ótima dos pontos e a distância total da rota.

Nota: Para alterar os pontos de entrega, você precisará editar a matriz de coordenadas diretamente dentro do arquivo calcular-melhor-rota.py.


### 2. Visualizar o gráfico de tempo de processamento do algoritmo

▶️ **Para executar, use o comando:**
```bash
python grafico-processamento.py
```
Saída esperada: Uma janela se abrirá mostrando o gráfico do tempo de processamento do problema em questão

### 3. Visualizar o gráfico de complexidade 

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
