# -*- coding: utf-8 -*-

def palindromo(palabra):
    #palabra = palabra.strip()
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_al_reves = palabra[::-1]
    if palabra == palabra_al_reves:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()

