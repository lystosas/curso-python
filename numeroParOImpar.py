def parImpar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def imprimir(valor, numero):
    if valor == True:
        print(f"El numero: {numero} es par\n")
    else:
        print(f"El numero: {numero} es impar\n")


inicio = True

while inicio:
    print("App que responde si el numero ingresado es par o impar\n".center(80))
    opcion = int(input(f"Seleccione:\n" f"1. Digitar numero\n" f"2. Salir\n->"))

    if opcion == 1:
        numero = int(input("Proporcione el numero a consultar: "))
        if numero > 0:
            resultado = parImpar(numero)
            imprimir(resultado, numero)
        else:
            print(f"El numero: {numero} digitado no es valido")
    elif opcion == 2:
        print("Saliendo de la App ....")
        inicio = False
    else:
        print(f"Opcion: {opcion} no es valida\n")
