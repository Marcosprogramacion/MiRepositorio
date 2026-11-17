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
    
    for i in range(len(lista_frase)):
        contador += 1
        letra:str = lista_frase[i]
        if contador == 1:
            lista_cifrado1.extend(letra)
        if contador == 2:
            lista_cifrado2.extend(letra)
        if contador == 3:
            lista_cifrado3.extend(letra)
        if contador == 4:
            lista_cifrado2.extend(letra)
            contador = 0

    cadena_1:str = "".join(lista_cifrado1)
    cadena_2:str = "".join(lista_cifrado2)
    cadena_3:str = "".join(lista_cifrado3)

    return cadena_1 + cadena_2 + cadena_3

def main():

    if len(sys.argv) != 2:
        print("número de argumentos no válido", file=sys.stderr)
        return

    alfabeto:list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    #Entrada
    frase:str = str(sys.argv[1].upper())    

    #Validacion
    for caracter in frase:
        if caracter not in alfabeto and caracter != " ":
            raise ValueError("Formato incorrecto")
        
    #Quitar espacios
    cadena:str = ""
    for caracter in frase:
        if caracter != " ":
            cadena += caracter

    #Salida
    resultado = cifrado(cadena)
    print(resultado)
    

if __name__ == "__main__":
    """Ejecuta el programa"""
    main()