"""En este programa el usuario introduce dos numeros en binario 
y pregunta si los resta o los suma. Posteriormente realiza la operación"""
#Entrada
lista_operando1:str = []
lista_operando2:str = []
lista_acarreo:str =[]
lista_resultado:str = []
binario1:str = input("Dime un numero binario de 8 bits: ")
binario2:str = input("Dime otro numero binario de 8 bits: ")
operacion:str = input("Dime si sumas (+) o si restas (-): ")
numeros_posibles:str = "10"
operaciones_posibles:str = "+-"
mensaje_formato_incorrecto:str = "Formato incorrecto"
#Calculo
lista_operando1.append(binario1)
lista_operando2.append(binario2)
if len(lista_resultado) < 9:
        for i in range(len(lista_resultado)):
            lista_resultado.insert(i,"0")
def formato_lista(lista_operando1,lista_operando2):
    if len(lista_operando1) > 8 or len(lista_operando2) > 8:
        return mensaje_formato_incorrecto
    
def suma(binario1,binario2,lista_operando1,lista_operando2):
    for i in range(len(lista_operando1)) and range(len(lista_operando2)):
        if binario1 == 0 and binario2 == 0:
            lista_acarreo.insert(i,"0")
            lista_resultado.insert(i,"0")
        elif binario1 == 1 and binario2 == 0:
            lista_acarreo.insert(i,"0")
            lista_resultado.insert(i,"1")
        elif binario1 == 0 and binario2 == 1:
            lista_acarreo.insert(i,"0")
            lista_resultado.insert(i,"1")
        else:
            lista_acarreo.insert(i,"1")
            lista_resultado.insert(i,"0")
        if lista_acarreo[i] == "1":
            if binario1 == 0 and binario2 == 0:
                lista_acarreo.insert(i,"0")
                lista_resultado.insert(i,"1")
            elif binario1 == 1 and binario2 == 0:
                lista_acarreo.insert(i,"1")
                lista_resultado.insert(i,"0")
            elif binario1 == 0 and binario2 == 1:
                lista_acarreo.insert(i,"1")
                lista_resultado.insert(i,"1")
            else:
                lista_acarreo.insert(i,"1")
                lista_resultado.insert(i,"1")
    return lista_resultado
    #La suma no esta bien hecha
def main():
    """Ejecuta la tarea principal del programa."""
    #Salida
    if operacion == "+":
        print(suma(binario1,binario2,lista_operando1,lista_operando2))
    else:
        return 

if __name__ == "__main__":
    # Solo se ejecuta al lanzar directamente este archivo.
    main()
else:
    # El módulo también puede ser importado por otro programa.
    print("Módulo importado")
    