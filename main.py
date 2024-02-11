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


def conversion_coulomb(carga, unidad):
    if unidad.lower() == "c":  # coulomb
        return carga
    elif unidad.lower() == "gc":  # gigacoulomb
        return carga * 1e9
    elif unidad.lower() == "mgc":  # megacoulomb
        return carga * 1e6
    elif unidad.lower() == "kc":  # kilocoulomb
        return carga * 1e3
    elif unidad.lower() == "mc":  # milicoulomb
        return carga * 1e-3
    elif unidad.lower() == "uc":  # microcoulomb
        return carga * 1e-6
    elif unidad.lower() == "nc":  # nanocoulomb
        return carga * 1e-9
    elif unidad.lower() == "pc":  # picocoulomb
        return carga * 1e-12
    else:
        raise ValueError("El valor no coincide con ninguna unidad válida. Verifica el input.")


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

    # Listas para los valores
    cargas = []
    fuerzas = []

    # Obtener datos de las cargas
    for i in range(3):
        carga = float(input(f"Ingrese el VALOR de la CARGA {i+1}: "))
        unidad = input("¿En qué unidad de Coulomb se encuentra la carga ("
                       "gigacoulomb = gc, megacoulomb = mgc, kilocoulomb = kc, coulomb = c, milicoulomb = mc, "
                       "microcoulomb = uc, nanocoulomb = nc, picocoulomb = pc)? ")
        cargas.append(conversion_coulomb(carga, unidad))

    # Obtener la distancia entre cada par de cargas
    distancias = []
    for i in range(2):
        distancia = float(input(f"Ingrese la DISTANCIA entre la carga {i+1} y la carga {i+2}: "))
        unidad = input("¿En qué unidad ingreso la distancia (mm, cm, m, km)? ")
        distancias.append(convertir_a_metros(distancia, unidad))

    # Calcular las fuerzas entre cada par de cargas mediante la formula de Coulomb
    for i in range(len(cargas) - 1):
        fuerza = calcular_fuerza(cargas[i], cargas[i + 1], distancias[i])
        # Calcular el ángulo respecto al eje horizontal (eje X)
        angulo = math.atan2(distancias[i], distancias[i]) * (180 / math.pi)
        # Descomposicion de los angulos para obtener magnitud de FRx y Fry
        vector_x = fuerza * math.cos(angulo)
        print(f"FRx = {vector_x}")
        vector_y = fuerza * math.sin(angulo)
        print(f"FRy = {vector_y}")
        fuerzas.append([vector_x, vector_y])

    # Calcular FR
    fuerza_resultante = calcular_fuerza_resultante(fuerzas)

    # Obtener magnitud y direccion de la fuerza resultante
    magnitud, direccion = calcular_magnitud_direccion(fuerza_resultante)

    # Impresión de todos los resultados
    print(f"La fuerza electroestatica es: {fuerza} N")
    print(f"La fuerza resultante en el eje X es: {fuerza_resultante[0]} N")
    print(f"La fuerza resultante en el eje Y es: {fuerza_resultante[1]} N")
    print(f"La magnitud de la fuerza resultante es: {magnitud} N")
    print(f"La direccion del vector formado por la FR es: {direccion} con respecto al eje X positivo")


if __name__ == "__main__":
    main()
