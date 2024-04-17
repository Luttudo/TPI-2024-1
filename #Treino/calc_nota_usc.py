P1 = float(input('insira nota da p1:'))
P2 = float(input('insira nota da p2:'))
out = float(input('insira nota de outros:'))
qui = float(input('insira nota de quiz:'))
tra = float(input('insira nota de trabalhos:'))

#Média final
mediax = ((P1 + P2)/2)*0.5
print(f"media das provas é {mediax}")
outx = out*0.1
quix = qui*0.1
trax = tra*0.3

print(f'sua média final é {mediax+outx+quix+trax}')