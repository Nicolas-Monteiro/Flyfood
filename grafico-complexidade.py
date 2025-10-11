import matplotlib.pyplot as plt
import numpy as np
import math

N_valores = np.arange(1, 11)

linear = N_valores

quadratica = N_valores ** 2

fatorial = [math.factorial(n) for n in N_valores]

plt.figure(figsize=(12, 7))

plt.plot(N_valores, linear, 
         label='$O(N)$ (Linear)', 
         marker='o', linestyle='-', linewidth=2, color='green')

plt.plot(N_valores, quadratica, 
         label='$O(N^2)$ (Quadrática)', 
         marker='s', linestyle='-', linewidth=2, color='blue')

plt.plot(N_valores, fatorial, 
         label='$O(N!)$ (Fatorial - Força Bruta)', 
         marker='^', linestyle='--', linewidth=3, color='red')


plt.yscale('log') 
plt.title('Comparação de Crescimento de Complexidade: PCV (O(N!)) vs. Polinomial', fontsize=16)
plt.xlabel('N (Tamanho da Entrada / Número de Pontos)', fontsize=14)
plt.ylabel('Número de Operações (Escala Logarítmica)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.xticks(N_valores)
plt.tight_layout()


plt.show()