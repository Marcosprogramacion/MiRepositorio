"""Modulo que lee un numero binario y comprueba si se lee igual de izquierda a derecha que de derecha a izquierda."""
# Marcos Martin Reinon fecha: 05/11/2022
def validacion(numero:str) -> bool:
    casos_posibles:str = "10"
        #Cálculo
    for n in numero:
        if n not in casos_posibles:
            return False

def palindromo(numero:str) -> str:
    
    izquierda:int = 0
    derecha:int = len(numero) - 1
    while izquierda < derecha:
        if numero[izquierda] == numero[derecha]:
            izquierda += 1
            derecha -= 1
        else:
            return "No es un palindromo"
    return "Es un palindromo"
        
import sys

def main():
    if len(sys.argv) != 2:
        print("número de argumentos no válido", file=sys.stderr)
        return

    #Entrada
    numero = sys.argv[1]

    #Salida
    if validacion(numero) == False:
        print("Formato incorrecto")
    else:
        resultado:str = palindromo(numero)
        print(resultado, file=sys.stderr)

if __name__ == "__main__":
    """Ejecuta programa"""
    main()
else:
    print("módulo importado")