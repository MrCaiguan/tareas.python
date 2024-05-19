contador_sueldo_1 = 0
contador_sueldo_2 = 0
total_sueldo = 0


print("ingrese el sueldo del empleador, entre $500.000 a $1.500.000 (ingrese -1 para terminar):")
while True:
    sueldo = int(input("ingrese sueldo del empleado: "))
    if sueldo==-1:
        break
    total_sueldo=total_sueldo+sueldo
    if sueldo>=500000 and sueldo<=900000:
     contador_sueldo_1=contador_sueldo_1+1
    if sueldo>900000:
     contador_sueldo_2=contador_sueldo_2+1



print("los empleados que ganan entre $500.000 a 900.000 son: ",contador_sueldo_1)
print("los empleados que ganan mas de $900.000 son: ",contador_sueldo_2)
print("el gasto total de la empresa en sueldos es: ",total_sueldo)

