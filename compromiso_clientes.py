def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


sesiones = [
    [101, 240, 12],
    [102, 45, 5],
    [103, 120, 6],
    [104, 200, 2],
    [105, 180, 8],
    [106, 60, 3],
    [107, 181, 9]
]

print("INFORME DE COMPROMISO")

for sesion in sesiones:
    cliente, duracion, clics = sesion
    nivel = clasificar_compromiso(duracion, clics)
    print(f"Cliente {cliente}: {nivel}")