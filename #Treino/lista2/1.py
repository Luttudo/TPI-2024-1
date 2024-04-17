def contador_vogais(string):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in string:
        if letra in vogais:
            contador += 1

    return contador

frase = "Estamos contando as vogais"
resultado = contador_vogais(frase)
print(f"A string '{frase}' possui {resultado} vogais")

