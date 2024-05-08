def validar(tel):
    if not tel.isnumeric():
        return False
    if len(tel) > 11 or len(tel) < 8:
        return False
    return True
validar('111')
validar('111333555')
validar('11133aaa5')

a = input('digite um telefone: ')
while not validar(a):
    a = input('digite um telefone: ')
