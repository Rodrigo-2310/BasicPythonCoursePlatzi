# -*- coding: utf-8 -*-

menu = """"

Bienvenido al conversor de monedas  

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: 

"""

opcion = input(menu)

if opcion == 1:
    pesos = float(input('¿Cuantos pesos colombianos tienes?: '))
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')
elif opcion == 2:
    pesos = float(input('¿Cuantos pesos argentinos tienes?: '))
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')
elif opcion == 3:
    pesos = float(input('¿Cuantos pesos mexicanos tienes?: '))
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')
else:
    print('Por favor ingresa una opcion correcta...')