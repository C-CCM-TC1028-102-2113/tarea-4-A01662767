def main():
    #escribe tu código abajo de esta línea
    print("NUMERO CON DIJITOS")
    n = int(input("CANTIDAD DE NUMEROS: "))
 
    for i in range(n):

        if i %2==0:
            print(i, "-%")
        else:
            print(i, "-#")

    pass
if __name__=='__main__':
    main()
