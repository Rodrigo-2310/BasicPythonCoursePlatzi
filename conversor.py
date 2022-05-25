### --- Programa para convertir pesos comlombianos a dólares --- ###

# Le pido al usuario la cantidad de pesos colombianos que tiene.
pesos = float(input('How many colombian pesos do you have?: '))

# Equivalencia de un dolar a pesos colombianos.
valor_dolar = 3875

# Realizo el cálculo.
dolares = pesos / valor_dolar

# Establezco el numero de decimales que quiero.
dolares = round(dolares, 2)

# Convierto el resultado a una cadena para poderla mostrar.
dolares = str(dolares)

# Muestro el resultado de la conversión.
print('You have $' + dolares + ' dollars')