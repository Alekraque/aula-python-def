#codigo "errado":
'''def validarCarros(carros):
    a = input('fala um carro ai: ')
    for b in carros:
        while a != b:
            a = input('fala um carro ai: ')
    return validarCarros()

validarCarros(['opala',
             'kwid',
             'ferrari',
             'lancer'])'''

#codigo certo:

def carro(lista):
    a = input('fala um carro ai: ')
    while True:
        for carros in lista:
            if a == carros:
                return a
carro(['opala',
        'kwid',
        'ferrari',
        'lancer'])

