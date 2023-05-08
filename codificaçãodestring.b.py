def codificar_string(string):
    codificacao = {
        'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't',
        'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a',
        'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h',
        'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'
    }
    s_codificada = ''

    for letra in string:
        if letra in codificacao:
            s_codificada += codificacao[letra]
        else:
            s_codificada += letra
    return s_codificada

string = 'o rato roeu a roupa do rei de roma'

texto_codificado = codificar_string(string)
print(texto_codificado)
