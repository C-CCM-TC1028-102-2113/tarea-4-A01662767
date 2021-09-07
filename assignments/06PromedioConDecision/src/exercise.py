def main():
    #escribe tu código abajo de esta línea
    print("PROMEDIO")
    cantidad = 0
    sum = 0

    while (True):
        nota = float(input("LA NOTA ES DE: "))

        if (nota == -1):
            break

        cantidad = cantidad + 1
        sum = sum + nota
    promedio = sum/nota
    print("EL PROMEDIO ES DE: ", promedio)

    pass
if __name__=='__main__':
    main()
