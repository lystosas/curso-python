import random


def numAleatorio():
    return random.randint(0, len(abecedario) - 1)


def letra():
    return abecedario[numAleatorio()]


abecedario = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

contraseña = []
sumatoria = 0
inicio = True


while inicio:
    print("App Generador de Contraseña\n".center(100))

    opcion = int(
        input(f"Digite la opcion...\n" f"1. Generar conreaseña.\n" f"2. Salir.\n" f"=>")
    )

    if opcion == 1:
        minuscula = int(input("Indique número mínimo de minusculas: \n=>"))
        mayuscula = int(input("Indique número mínimo de mayusculas: \n=>"))
        numerico = int(input("Indique número mínimo de caracteres númericos: \n=>"))
        longitud = int(input("Indique longitud de la contraseña: \n=>"))

        total = minuscula + mayuscula + numerico
        if total <= longitud:
            if sumatoria <= longitud:
                while minuscula > 0:
                    if sumatoria == longitud:
                        break

                    contraseña.append(letra())
                    minuscula -= 1
                    sumatoria += 1

                while mayuscula > 0:
                    if sumatoria == longitud:
                        break

                    contraseña.append(letra().upper())
                    mayuscula -= 1
                    sumatoria += 1

                while numerico > 0:
                    if sumatoria == longitud:
                        break

                    contraseña.append(str(random.randint(1, 9)))
                    numerico -= 1
                    sumatoria += 1

            if sumatoria != longitud:
                minuscula, mayuscula, numerico = 1, 1, 1

            if sumatoria == longitud:
                break

            # Con random.shuffle desordeno el array
            random.shuffle(contraseña)

            # Con "".join(contraseña) extraigo los elemntos del array y creo una cadena
            clave = "".join(contraseña)

            print(f"SU CONTRASEÑA ES: {clave}")
        else:
            print("los datos de la contraseña son mayores que la longitud")
    elif opcion == 2:
        print(f"Saliendo de la App ...")
        inicio = False
    else:
        print("Opcion Invalida")
