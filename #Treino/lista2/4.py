def contador(frase, palavra):

    palavras = frase.split()

    contador = 0

    for p in palavras:

        p = p.lower()

        if p == palavra.lower():
            contador += 1
    
    return contador
        

