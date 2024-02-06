import math

# Convertir unidades de distancia a metros r = distancia,
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

