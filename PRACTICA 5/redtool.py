"""Enunciado"""
# Marcos Martin Reinon
import sys

def validar_ip(ip:str) -> bool:

    salida2: False
    if ip[0] >= 0 and ip[0] <= 256 and ip[1] >= 0 and ip[1] <= 256 and ip[2] >= 0 and ip[2] <= 256 and ip[3] >= 0 and ip[3] <= 256:
        salida2 = True
    return salida2

def salida_argv1(dar_ip:str) -> bool:

    salida1 = True
    if dar_ip != "-ip":
        salida1 = False
    return salida1 

def main():

    if len(sys.argv) != 3 or len(sys.argv) != 4:
        print("número de argumentos no válido", file=sys.stderr)
        return

    #Entrada
    dar_ip:str = sys.argv[1]
    ip:str = sys.argv[2].split(".")

    #Salida

    if salida_argv1(dar_ip) == False or validar_ip(ip) == False:
        print("formato no valido")

if __name__ == "__main__":
    """Ejecuta el programa"""
    main()