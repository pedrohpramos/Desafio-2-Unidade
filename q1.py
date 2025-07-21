lista = [True,False,True,False,True]

t=0
f=0

for i in lista:
    if i == True:
        t += 1
    else:
        f += 1

print(f"A quantiadde de valores True é de: {t}")
print(f"A quantidade de valores False é de: {f}")