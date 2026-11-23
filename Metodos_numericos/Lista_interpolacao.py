#Pedro Vitor de Souza Dantas

#Questão 1, na questão um, utilizei tanto os método por sistema linear quanto Lagrange

import numpy as np

# Pontos a tabela, usei numpy para melhor manejo
x = np.array([-0.50, -0.75, -1.00, -1.50])
y = np.array([-2.80, -0.60, 1.00, 3.20])

# Montando a matriz
A = np.vander(x, increasing=True)  # cada linha: [1, x, x², x³]

# Resolvendo o sistema linear
coef = np.linalg.solve(A, y)

# Coeficientes do polinômio
a0, a1, a2, a3 = coef
print(f"Coeficientes do polinômio P(x):")
print(f"a0 = {a0:.5f}, a1 = {a1:.5f}, a2 = {a2:.5f}, a3 = {a3:.5f}")

# Função para avaliar o polinômio
def P(x_val):
    return a0 + a1*x_val + a2*x_val**2 + a3*x_val**3

#Resolvendo por Lagrange
def lagrange_interpol(xi, yi, x_val):
    n = len(xi)
    result = 0
    for i in range(n):
        term = yi[i]
        for j in range(n):
            if i != j:
                term *= (x_val - xi[j]) / (xi[i] - xi[j])
        result += term
    return result

x_interp_lagrange = -0.82
y_interp_lagrange = lagrange_interpol(x, y, x_interp_lagrange)

# Interpolação em x = -0.82
x_interp = -0.82
y_interp = P(x_interp)
print("\nPor sistema linear:")
print(f"Interpolação por sistema linear em x = {x_interp}: y = {y_interp:.5f}")
print("\nPor Lagrange:")
print(f"Interpolação por Lagrange em x = {x_interp_lagrange}: y = {y_interp_lagrange:.5f}")


#Questão 2

import numpy as np
import matplotlib.pyplot as plt

# Dados originais (em ordem decrescente)
x_orig = np.array([-0.50, -0.75, -1.00, -1.50])
y_orig = np.array([-2.80, -0.60, 1.00, 3.20])

# Reordena os dados em ordem crescente
indices = np.argsort(x_orig)
x = x_orig[indices]
y = y_orig[indices]

print("x ordenado:", x)
print("y ordenado:", y)

def natural_cubic_spline_coeff(x, y):
    """
    Calcula os coeficientes do spline cúbico natural para os pontos (x, y).
    Retorna os vetores de coeficientes a, b, c, d para cada segmento
    onde o spline em cada intervalo [x_i, x_i+1] é dado por:
    
        S_i(x) = a_i + b_i*(x - x_i) + c_i*(x - x_i)**2 + d_i*(x - x_i)**3
    """
    n = len(x) - 1  # número de segmentos
    h = np.array([x[i+1] - x[i] for i in range(n)])
    
    # Passo 1: Calcular os vetores alpha (apenas para i=1,...,n-1)
    alpha = np.zeros(n + 1)
    for i in range(1, n):
        alpha[i] = (3/h[i])*(y[i+1] - y[i]) - (3/h[i-1])*(y[i] - y[i-1])
        
    # Passo 2: Resolver o sistema tridiagonal para os c's
    l = np.zeros(n + 1)
    mu = np.zeros(n + 1)
    z = np.zeros(n + 1)
    
    # Condições de contorno natural: c[0] = c[n] = 0
    l[0] = 1
    mu[0] = 0
    z[0] = 0
    
    for i in range(1, n):
        l[i] = 2*(x[i+1]-x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1]*z[i-1]) / l[i]
    
    l[n] = 1
    z[n] = 0
    c = np.zeros(n + 1)
    b = np.zeros(n)
    d = np.zeros(n)
    c[n] = 0
    
    # Passo 3: Calcular os coeficientes b e d (e já temos a = y)
    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (y[j+1]-y[j])/h[j] - h[j]*(c[j+1] + 2*c[j]) / 3
        d[j] = (c[j+1]-c[j]) / (3*h[j])
    
    # a são os valores de y em cada intervalo
    a = y[:-1]
    return a, b, c[:-1], d, x

def cubic_spline_eval(x_eval, a, b, c, d, x):
    """
    Interpola o valor em x_eval utilizando os coeficientes do spline
    para o intervalo onde x_eval se encontra. Assume que x está ordenado.
    """
    n = len(x) - 1
    # Encontrar o segmento i tal que: x[i] <= x_eval <= x[i+1]
    if x_eval <= x[0]:
        i = 0
    elif x_eval >= x[-1]:
        i = n - 1
    else:
        i = 0
        while i < n and x_eval > x[i+1]:
            i += 1
    dx = x_eval - x[i]
    return a[i] + b[i]*dx + c[i]*(dx**2) + d[i]*(dx**3)

# Calcular os coeficientes do spline
a, b, c, d, x_sorted = natural_cubic_spline_coeff(x, y)

# Valor a ser interpolado
x_interp = -0.82

# Interpolação usando o spline cúbico natural manual
y_interp_spline = cubic_spline_eval(x_interp, a, b, c, d, x_sorted)

print(f"\nSpline cúbico natural (manual) em x = {x_interp}: y = {y_interp_spline:.5f}")

# Para comparação, implementamos o polinômio de Lagrange (questão 1)
def lagrange_interpol(xi, yi, x_val):
    n = len(xi)
    result = 0
    for i in range(n):
        term = yi[i]
        for j in range(n):
            if i != j:
                term *= (x_val - xi[j]) / (xi[i] - xi[j])
        result += term
    return result

# Como a ordem dos pontos importa para Lagrange, usamos os dados originais (ou já ordenados)
# Aqui usaremos os dados ordenados também
y_interp_lagrange = lagrange_interpol(x_sorted, y[np.argsort(x_orig)], x_interp)
print(f"Polinômio de Lagrange em x = {x_interp}: y = {y_interp_lagrange:.5f}")

# Plot para visualizar os splines e a interpolação
x_plot = np.linspace(x_sorted[0], x_sorted[-1], 200)
y_plot = [cubic_spline_eval(x_val, a, b, c, d, x_sorted) for x_val in x_plot]

plt.figure(figsize=(8,5))
plt.plot(x_plot, y_plot, label="Spline Cúbico Natural (manual)", color="green")
plt.scatter(x_sorted, y[np.argsort(x_orig)], label="Dados", color="blue")
plt.scatter([x_interp], [y_interp_spline], label=f"Interpolado em {x_interp}", color="red", zorder=5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolação por Spline Cúbico Natural (manual)")
plt.legend()
plt.grid(True)
plt.show()

# Questão 3

import matplotlib.pyplot as plt

# Dados
anos = np.array([0, 3, 7, 11, 14, 18, 22, 26, 28, 29, 35, 37, 41, 46, 49, 51])
transistores = np.array([
    2300, 6000, 29000, 120000, 275000, 1200000, 3100000, 7500000,
    24000000, 42000000, 291000000, 731000000, 1400000000,
    4800000000, 16000000000, 20000000000
])

# log2
log2_y = np.log2(transistores)

# Regressão
coef = np.polyfit(anos, log2_y, 1)
modelo = np.poly1d(coef)

# Previsão para 2026 (ano 55)
ano_prev = 55
log2_pred = modelo(ano_prev)
pred = 2 ** log2_pred
print(f"Previsão para 2026: {pred:.2e} transistores")

# Gráfico
plt.figure(figsize=(10,6))
plt.scatter(anos, log2_y, color='blue', label='Dados log2')
plt.plot(anos, modelo(anos), color='red', label='Ajuste linear')
plt.xlabel("Ano (desde 1971)")
plt.ylabel("log2(Transistores)")
plt.title("Lei de Moore (Escala log2)")
plt.legend()
plt.grid(True)
plt.show()
