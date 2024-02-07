import math


# Convertir unidades de distancia a metros (r = distancia)
def convertir_a_metros(r, unidad):
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
def calcular_fuerza(q1, q2, r):
    k = 9e9  # Constante de Coulomb 9x10^9 Nm^2/C^2
    return k * abs(q1) * abs(q2) / (r ** 2)


def calcular_fuerza_resultante(fuerzas):
    fuerza_resultante = [0, 0]  # Inicia al centro del plano
    for fuerza in fuerzas:
        fuerza_resultante[0] += fuerza[0]  # Suma de las Fuerzas en eje x
        fuerza_resultante[1] += fuerza[1]  # Suma de las Fuerzas en eje y
    return fuerza_resultante


# Obtener magnitud y direccion de la fuerza resultante
def calcular_magnitud_direccion(fuerza):
    magnitud = math.sqrt(fuerza[0] ** 2 + fuerza[1] ** 2)
    direccion = math.atan2(fuerza[1], fuerza[0]) * (180 / math.pi)
    return magnitud, direccion


def main():
    num_cargas = int(input("Ingrese el número de cargas (máximo 4): "))

    if 2 <= num_cargas <= 4:
        print("Número de cargas inválido. Debe estár en un rango de 2 a 4.")

    # Listas para los valores
    cargas = []
    distancias = []
    fuerzas = []

    # Obtener datos de las cargas
    for i in range(num_cargas):
        carga = float(input(f"Ingrese el VALOR de la CARGA {i+1} (en Coulombs): "))
        cargas.append(carga)

        if i > 0:
            distancia = float(input(f"Ingrese la DISTANCIA entre la carga {i} y la carga {i+1}: "))
            unidad = input("¿En qué UNIDAD se ingreso la distancia (m, cm, mm, km)? ")
            distancias.append(convertir_a_metros(distancia, unidad))

    # Calcular las fuerzas entre cada par de cargas mediante la formula de Coulomb.
    for i in range(len(cargas) - 1):
        distancia = distancias[i]
        fuerza = calcular_fuerza(cargas[i], cargas[i + 1], distancia)
        # Obtener el angulo con respecto a la horizontal en eje X
        angulo = math.atan2(cargas[i + 1], cargas[i]) * (180 / math.pi)
        # Descomposicion de los angulos para obtener magnitud de FRx y Fry
        vector_x = fuerza * math.cos(angulo)
        vector_y = fuerza * math.sin(angulo)
        fuerzas.append([vector_x, vector_y])

    # Calcular FR
    fuerza_resultante = calcular_fuerza_resultante(fuerzas)

    # Obtener magnitud y direccion de la fuerza resultante
    magnitud, direccion = calcular_magnitud_direccion(fuerza_resultante)

    # Impresión de todos los resultados
    print(f"La fuerza resultante en el eje X es: {fuerza_resultante[0]} N")
    print(f"La fuerza resultante en el eje Y es: {fuerza_resultante[1]} N")
    print(f"La magnitud de la fuerza resultante es: {magnitud} N")
    print(f"La direccion del vector formado por la FR es: {direccion} con respecto al eje X positivo")


if __name__ == "__main__":
    main()
