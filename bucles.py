
def run():
    limite = int(input('Ingresa el límite que quieras: '))
    contador = 0
    while limite >= contador:
        potencia = 2**contador
        print('2 elevado a la ' + str(contador) + ' es igual a: ' + str(potencia))
        contador = contador + 1

if __name__ == '__main__':
    run()