a = [100, 300, 28, 8243]
def maiorNumero(numeros):
    maior = 0
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

print(maiorNumero(a))






