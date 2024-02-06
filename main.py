import math


# Convertir unidades de distancia a metros r = distancia
def convert_to_meters(r, unidad):
    if unidad.lower() == "m":
        return r
    elif unidad.lower() == "cm":
        return r / 100
    elif unidad.lower() == "mm":
        return r / 1000
    elif unidad.lower() == "km":
        return r * 1000
    else:
        raise ValueError("Unidad de distancia no valida. Ingrese m, cm, mm o km")


# Función para obtener fuerza electroestática entre dos cargas
def calculate_force(q1, q2, r):
    k = 9e9  # Constante de Coulomb 9x10^9 Nm^2/C^2
    return k * abs(q1) * abs(q2) / (r ** 2)


def calcular_fuerza_resultante(fuerza):
    fuerza_resultante = [0][0]  # Inicia al centro del plano
    for fuerza in fuerzas:
        fuerza_resultante[0] += fuerza[0]  # Suma de las fuerzas en eje x
        fuerza_resultante[1] += fuerza[1]  # Suma ed las fuerzas en eje y
    return fuerza_resultante
