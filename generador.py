import random

print('*******GENERADOR DE CONTRASEÑAS***********')

minimo = int(input('Indique número mínimo de minusculas: '))
# maximo = int(input('Indique número mínimo de mayusculas: '))
# numerico = int(input('Indique número mínimo de caracteres númericos: '))
# longitud = int(input('Indique longitud de la contraseña: '))

abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

contrasena = []

def numAleatorio():
    return random.randint(0, len(abecedario) - 1)    

def letra():
    return abecedario[numAleatorio()]




    letras = letra()
    contrasena.append(letras)


print(contrasena)