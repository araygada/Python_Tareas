# Ejercicio 1.2 - Alberto Raygada
# Program que encuentre todos los numero primos entre 10 y 90
# ---------------------------------------------------------------------------------------

primos = [i for i in range(10,90) if (i%2!=0 or i ==2) and (i%3!=0 or i==3) and (i%5!=0 or i==5) and (i%7!=0 or i==7)]
print(primos)


