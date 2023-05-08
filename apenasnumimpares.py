def numeros_impares(numero):
    if numero % 2 == 0:
        print(f'O numero {numero} é par.')
        num_pares.append(numero)
    else:
        print(f' O numero {numero} é impar')
        num_impares.append(numero)

num_pares = []
num_impares = []

for numero in range(1, 101):
    numeros_impares(numero)

print(f'Numeros impares: {num_impares}')
print(f'Numeros pares: {num_pares}')
