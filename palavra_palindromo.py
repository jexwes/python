

def palavra_palindromo(palavra):
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        print(f'A palavra {palavra} é um palindromo!')
    else:
        print(f'A palavra {palavra} não é um palindromo!')

palavras = ['reviver', 'radar', 'banana', 'arara', 'python']

for palavra in palavras:
    palavra_palindromo(palavra)
