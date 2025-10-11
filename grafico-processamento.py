import matplotlib.pyplot as plt
import numpy as np

N_pontos = [4, 5, 6, 7, 8, 9, 10, 11]
tempo_segundos = [0.0001, 0.0005, 0.0036, 0.025, 0.20, 1.8, 18.5, 203.0]

plt.figure(figsize=(10, 6))
plt.plot(N_pontos, tempo_segundos, marker='o', linestyle='-', color='red')

plt.yscale('log') 
plt.title('Crescimento Fatorial do Tempo de Processamento (O(N!))')
plt.xlabel('N (Número de Pontos de Entrega)')
plt.ylabel('Tempo de Processamento Médio (segundos - Escala Logarítmica)')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.xticks(N_pontos)
plt.tight_layout()
plt.show()