'''def podeVotar(nome, idade):
    if idade >=16:
        print(f'a pessoa {nome} pode votar')
        return True
    else:
        print(f'  a peesoa {nome} nao pode votar')
        return False


a = podeVotar('lucas', 38)
print(f' a primeira resposta foi {a}')
b = podeVotar('maira', 13)
print(f'   a seguda resposta foi {b}')'''

def nascimento(ano):
    return 2024 - ano

ano = input('diga seu ano de nascimento: ')
while not (ano.isnumeric() and len(ano) == 4):
    print('insira um numero inteiro de 4 digitos')
    ano = input('diga seu ano de nascimento: ')
ano = int(ano)

idade = nascimento(ano)
print(f'você tem {idade} anos')
