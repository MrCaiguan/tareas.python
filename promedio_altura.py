contador_alturas = 0
suma_alturas = 0


print("Ingrese las alturas de las personas en metros (ingrese 0 para terminar):")
altura = float(input("Altura (metros): "))
while altura != 0:
    suma_alturas = suma_alturas + altura
    contador_alturas = contador_alturas + 1
    altura = float(input("Altura (metros): "))

if contador_alturas != 0:
    altura_promedio = suma_alturas / contador_alturas
    print("La altura promedio de las personas es:", altura_promedio, "metros")
else:
    print("No se ingresaron alturas.")