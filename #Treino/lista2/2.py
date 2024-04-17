def substituidor(string, letra_antiga, letra_nova):
    nova_string = string.replace(letra_antiga, letra_nova)
    return nova_string

frase = "Esta frase vai substituir alguma letra"
letra_antiga = "A"
letra_nova = "X"
resultado = substituidor(frase, letra_antiga, letra_nova)

print(resultado)


def substituir_letra(string, letra_antiga, letra_nova):
    nova_string = string.replace(letra_antiga, letra_nova)
    return nova_string

frase = "Esta frase vai substituir alguma letra"
letra_antiga = "a"
letra_nova = "X"
resultado = substituir_letra(frase, letra_antiga, letra_nova)

# print(resultado)

# def substituidor_insensivel(string, letra_antiga, letra_nova):
#     nova_string = string.replace(letra_antiga.lower(), letra_nova.lower())
#     return nova_string


