lista = [1,2,3,4,5,6,7,8,9,10]
soma_os_pares = []

for numero in range(0, len(lista)-1, 2):
    soma = lista[numero] + lista[numero+1]
    soma_os_pares.append(soma)
if len(lista) % 2 != 0:
    soma_os_pares.append(lista[-1])

maior_soma = max(soma_os_pares)

for soma in soma_os_pares:
    print(soma)

print(f"A maior soma do vetor é: {maior_soma}")
print (soma_os_pares)



