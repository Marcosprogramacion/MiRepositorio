"""Modulo que lee un numero binario y comprueba si se lee igual de izquierda a derecha que de derecha a izquierda."""
# Marcos Martin Reinon fecha: 03/11/2022
def validacion(numero:str) -> bool:
    casos_posibles:str = "10"
    for n in numero:
        if n not in casos_posibles:
            return False

def palindromo(numero:str) -> str:
    lista_derecho:list = []
    lista_reves:list = []
    
    #Calculo
    for i in numero:
        lista_derecho.extend(i)
    for k in numero[::-1]:
        lista_reves.extend(k)
    if lista_derecho == lista_reves:
        return "Es un palindromo"
    else:
        return "No es un palindromo"
        
            

import sys

def main():
    if len(sys.argv) != 2:
        print("número de argumentos no válido", file=sys.stderr)
        return

    #Entrada
    numero = sys.argv[1]

    #Salida
    if validacion(numero) == False:
        return "Formato incorrecto"
    else:
        resultado = palindromo(numero)
        print(resultado, file=sys.stderr)

if __name__ == "__main__":
    """Ejecuta programa"""
    main()
else:
    print("módulo importado")
