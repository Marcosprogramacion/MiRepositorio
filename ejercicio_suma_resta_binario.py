"""En este programa el usuario introduce dos numeros en binario 
y pregunta si los resta o los suma. Posteriormente realiza la operación"""
#Entrada
lista_operando1:list = []
lista_operando2:list = []
lista_acarreo:list =[0,0,0,0,0,0,0,0,0]
lista_resultado:list = []
binario1:str = input("Dime un numero binario de 8 bits: ")
binario2:str = input("Dime otro numero binario de 8 bits: ")
operacion:str = input("Dime si sumas (+) o si restas (-): ")
numeros_posibles:str = "10"
operaciones_posibles:str = "+-"
mensaje_formato_incorrecto:str = "Formato incorrecto"
#Calculo
lista_operando1.extend(binario1)
lista_operando2.extend(binario2)

def formato_lista(lista_operando1,lista_operando2):
    if len(lista_operando1) > 8 or len(lista_operando2) > 8:
        return mensaje_formato_incorrecto
    
def suma(lista_operando1,lista_operando2):
    for i in range(len(lista_operando1))[::-1]:
        if lista_operando1[i] == "0":
            lista_operando1.insert(i,"0")
        elif lista_operando1[i] == "1":
            lista_operando1.insert(i,"1")  
    
    for i in range(len(lista_operando2))[::-1]:
        if lista_operando2[i] == "0":
            lista_operando2.insert(i,"0")
        elif lista_operando2[i] == "1":
            lista_operando2.insert(i,"1")

    #La suma no esta bien hecha (Voy a hacer los for por separado)
def main():
    """Ejecuta la tarea principal del programa."""
    #Salida
    if operacion == "+":
        print(suma(lista_operando1,lista_operando2))
    else:
        return 

if __name__ == "__main__":
    # Solo se ejecuta al lanzar directamente este archivo.
    main()
else:
    # El módulo también puede ser importado por otro programa.
    print("Módulo importado")
    