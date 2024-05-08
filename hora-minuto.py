def proxHorario(hora, minuto):
    if minuto == 59:
        minuto = 0

        if hora == 23:
            hora = 0
        else:
            hora += 1
    else:
        minuto +=1
    return f'{hora}h{minuto}'

a = proxHorario(23, 59)
print(a)

a = proxHorario(21, 59)
print(a)

a = proxHorario(23, 29)
print(a)
