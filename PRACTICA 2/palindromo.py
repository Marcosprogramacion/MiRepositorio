"""Modulo que lee un numero binario y comprueba si se lee igual de izquierda a derecha que de derecha a izquierda."""
# Marcos Martin Reinon fecha: 03/11/2022
import sys

def palindromo(numero:int,lista_numero:list) -> str:

    lista_numero = lista_numero.extend(numero)
    #Cálculo
    if 1 not in numero or 0 not in numero:
        return "Formato incorrecto"
    else:
        if lista_numero[::1] != lista_numero[::-1]:
            return "No es palindromo"
        else:
            return "Es palindromo"

def main():

    #Entrada
    lista_numero:list = []
    numero:int = int(sys.argv[1])
    resultado:str = palindromo(numero,lista_numero)
    if len(sys.argv) != 2:
        print("número de argumentos no válido")
    else:
        
        #Salida
        print(resultado)

if __name__ == "__main__":
    """Ejecuta programa"""
    main()
else:
    print("módulo importado")
