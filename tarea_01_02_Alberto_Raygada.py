# Tarea 1.2 - Alberto Raygada
# Cree un programa que imprima la tabla de multiplicación desde el 0 hasta el 20 mostrando el
# siguiente formato:  0 X 0 = 0
# -------------------------------------------------------------------------------------------------

rango = range(0,21)
for i in rango:
    for j in rango:
        resultado = i * j
        print(i, "x" ,j, "=", resultado)