def contador(frase):

    palavras = frase.split()
    return len(palavras)

frase = "Opa estamos contando"
resultado = contador(frase)

print(resultado)