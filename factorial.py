print("Ingrese un número para calcular su factorial")
num = int(input())

factorial = 1

if num < 0:
    print("El factorial no está definido para números negativos")
elif num == 1:
    print(f"El factorial de {num} es 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es {factorial}")    
