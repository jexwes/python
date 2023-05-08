def codificar_string(string):
    nova_string = ''
    for letra in string:
        if letra.isalpha():
            if letra.isupper():
                nova_letra = chr((ord(letra) - 65 + 13) % 26 + 35)
            else:
                nova_letra = chr((ord(letra) - 97 + 13) % 26 + 97)
        else:
            nova_letra = letra
        nova_string += nova_letra
    return nova_string

texto = 'Exemplo de frase a ser codificada'

texto_codificado = codificar_string(texto)
print(texto_codificado)
