import csv
from typing import List, Tuple
import numpy as np

def ler_csv(caminho: str) -> Tuple[List[float], List[float], List[float]]:
    densidade, fluxo, velocidade = [], [], []
    with open(caminho, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            densidade.append(float(row["density"]))
            fluxo.append(float(row["flow"]))
            velocidade.append(float(row["velocity"]))
    return densidade, fluxo, velocidade

def resolver_sistema(A: List[List[float]], b: List[float]) -> List[float]:
    return np.linalg.solve(np.array(A), np.array(b)).tolist()

def r2(y_true: List[float], y_pred: List[float]) -> float:
    media = sum(y_true) / len(y_true)
    ss_tot = sum((y - media) ** 2 for y in y_true)
    ss_res = sum((y - y_hat) ** 2 for y, y_hat in zip(y_true, y_pred))
    return 1 - ss_res / ss_tot

def r2_ajustado(r2: float, n: int, p: int) -> float:
    return 1 - ((1 - r2) * (n - 1)) / (n - p - 1)

def ajuste_linear(x: List[float], y: List[float]) -> Tuple[List[float], float, float]:
    n = len(x)
    A = [
        [sum(xi ** 2 for xi in x), sum(x)],
        [sum(x), n]
    ]
    b = [sum(x[i] * y[i] for i in range(n)), sum(y)]
    coef = resolver_sistema(A, b)
    y_pred = [coef[0] * xi + coef[1] for xi in x]
    r2_val = r2(y, y_pred)
    r2_adj = r2_ajustado(r2_val, n, 1)
    return coef, r2_val, r2_adj

def ajuste_cubico(x: List[float], y: List[float]) -> Tuple[List[float], float, float]:
    n = len(x)
    X = [[xi ** 3, xi ** 2, xi, 1] for xi in x]
    A = [[sum(xi[i] * xi[j] for xi in X) for j in range(4)] for i in range(4)]
    b = [sum(xi[i] * yi for xi, yi in zip(X, y)) for i in range(4)]
    coef = resolver_sistema(A, b)
    y_pred = [coef[0]*xi**3 + coef[1]*xi**2 + coef[2]*xi + coef[3] for xi in x]
    r2_val = r2(y, y_pred)
    r2_adj = r2_ajustado(r2_val, n, 3)
    return coef, r2_val, r2_adj

def exibir_resultados(nome, coef, r2_val, r2_adj):
    print(f"\nArquivo: {nome}")
    print("Coeficientes:", coef)
    print(f"R²: {r2_val:.5f}")
    print(f"R² Ajustado: {r2_adj:.5f}")

# Processamento dos arquivos
for arquivo in ["d:/Cursos/Códigos/Treinando/Faculdade/Métodos numéricos/dataset-foto.csv"]:
    x, y, v = ler_csv(arquivo)

    # Ajuste linear: flow = a * density + b
    coef_lin, r2_lin, r2adj_lin = ajuste_linear(x, y)
    exibir_resultados(arquivo + " - Linear (Fluxo vs Densidade)", coef_lin, r2_lin, r2adj_lin)

    # Ajuste cúbico: velocity = a*density^3 + b*density^2 + c*density + d
    coef_cub, r2_cub, r2adj_cub = ajuste_cubico(x, v)
    exibir_resultados(arquivo + " - Cúbico (Velocidade vs Densidade)", coef_cub, r2_cub, r2adj_cub)
