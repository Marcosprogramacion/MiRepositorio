"""Este programa pedira un numero llamado rotacion y una frase y la encriptara utilizando el método cesar"""
import sys

alfabeto:list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfabeto_cifrado:list = []
def cifrado(rotacion:int, frase:str) -> str:

    #Calculo
    for i in range(len(alfabeto)):
        posicion:int = i
        cambio1:str = alfabeto[posicion]
        desplazamiento:int = (posicion + rotacion) % len(alfabeto)
        cambio2:str = alfabeto[desplazamiento]
        aux:str = cambio1
        cambio1 = cambio2
        cambio2 = aux
        cambio_total = ", ".join(cambio1,cambio2)
        alfabeto_cifrado.extend(cambio_total)
        

        

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