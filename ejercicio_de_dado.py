import random

def simular_lanzamientos(cantidad):
    eventos = [1, 2, 3, 4, 5, 6]
    resultados = [random.choice(eventos) for _ in range(cantidad)]
    print(f"--- Resultados de {cantidad} lanzamientos de un dado ---")
    for i, resultado in enumerate(resultados, 1):
        print(f"Lanzamiento {i}: {resultado}")
    conteo = {cara: resultados.count(cara) for cara in eventos}
    print("\nConteo por cara:")
    for cara, total in conteo.items():
        print(f"Cara {cara}: {total}")

simular_lanzamientos(5)