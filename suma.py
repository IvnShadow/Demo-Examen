numeros = []
i = 0
suma = 0
while i < 2:
    valor = float(input("Ingrese un número: "))
    numeros.append(valor)

    suma = suma + numeros[i]

    i= i + 1

print("La suma es: ", suma)