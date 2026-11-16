"""Este programa consiste en replicar el método de cifrado de rail. Consiste en poner la frase en cigzag en 3 listas (en este caso) y sumar posteriormente el resultado para formar la frase"""
import sys

def cifrado(frase:str) -> list[list,list,list]:

    #Calculo
    lista_frase:list = []
    lista_frase.extend(frase)
    lista_cifrado1:list = []
    lista_cifrado2:list = []
    lista_cifrado3:list = []
    contador:int = 0
    contador_vuelta:int = 0
    
    while contador > -1:
        for i in lista_frase:
            if contador == 0:
                lista_cifrado1.extend(i)
                contador = 1
                continue
            if contador == 1:
                lista_cifrado2.extend(i)
                contador = 2
                continue
            if contador == 2:
                lista_cifrado3.extend(i)
                contador = 3
                continue
            if contador == 3:
                lista_cifrado2.extend(i)
                contador = 4
                continue
            if contador == 4:
                lista_cifrado1.extend(i)
                contador = 1    
        contador = -2

    lista_resultado:list = [lista_cifrado1, lista_cifrado2, lista_cifrado3] 
    return lista_resultado


def main():

    if len(sys.argv) != 2:
        print("número de argumentos no válido", file=sys.stderr)
        return

    #Entrada
    frase:str = sys.argv[1]

    #Salida
    cadena_resultado:str = ""
    for j in cifrado(frase):
        cadena_resultado = str(j) + cadena_resultado
    print(cadena_resultado)

if __name__ == "__main__":
    """Ejecuta el programa"""
    main()