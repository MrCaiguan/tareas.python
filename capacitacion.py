total_preguntas=int(input(" ingrese total de preguntas realizadas: "))
total_correctas=int(input(" ingrese cantidad de preguntas contestadas correctamente: "))
porcentaje=(total_correctas/total_preguntas)*100
if porcentaje>=95:
    print("nivel maximo")
if porcentaje>=70 and porcentaje<95:
    print("nivel medio")
if porcentaje>=40 and porcentaje<70:
    print("nivel regular")
if porcentaje<40:
    print("fuera de nivel")  

