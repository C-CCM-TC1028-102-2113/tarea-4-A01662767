import math
def main():
    #escribe tu código abajo de esta línea
    print("Número al cuadrado mayor que N")
    n = int(input("NUMERO: "))

    for i in [n]:
        cuadrado = math.sqrt(i)
        f= math.ceil(cuadrado)
        print (f)

    pass
if __name__=='__main__':
    main()
