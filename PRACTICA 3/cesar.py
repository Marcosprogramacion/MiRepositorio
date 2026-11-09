"""Este programa pedira un numero llamado rotacion y una frase y la encriptara utilizando el método cesar"""
import sys

alfabeto:list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfabeto_cifrado:list = []
def cifrado(rotacion:int, frase:str) -> str:

    #Calculo
    posicion:int = 0
    desplazamiento:int = (posicion + rotacion) % len(alfabeto)
    for i in alfabeto:
        aux:str = i
        aux2:str = alfabeto[desplazamiento]
        aux = aux2
        print(aux)

def main():
     
    if len(sys.argv) != 3:
        print("número de argumentos no válido", file=sys.stderr)
        return

    #Entrada
    rotacion:int = int((sys.argv[1]))
    frase:str = sys.argv[2]

    #Salida
    resultado = cifrado(rotacion,frase)
    print(resultado)

if __name__ == "__main__":
    main()