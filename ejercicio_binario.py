"""En este programa el usuario introduce dos numeros en binario 
y pregunta si los resta o los suma. Posteriormente realiza la operación"""
#Entrada
lista_operando1:list = []
lista_operando2:list = []
lista_acarreo_suma:list =["0","0","0","0","0","0","0","0","0"]
lista_acarreo_resta:list =["0","0","0","0","0","0","0","0","0"]
lista_resultado_suma:list = []
lista_resultado_resta:list = []
binario1:str = input("Dime un numero binario de 8 bits: ")
binario2:str = input("Dime otro numero binario de 8 bits: ")
operacion:str = input("Dime si sumas (+) o si restas (-): ")
numeros_posibles:str = "10"
operaciones_posibles:str = "+-" 
mensaje_formato_incorrecto:str = "Formato incorrecto"
#Calculo
lista_operando1.extend(binario1)
lista_operando2.extend(binario2)

while len(binario1) < 9:
    binario1 = "0" + binario1
lista_operando1.clear()
lista_operando1.extend(binario1)
lista_operando1 = lista_operando1[::-1]             

while len(binario2) < 9:
    binario2 = "0" + binario2
lista_operando2.clear()
lista_operando2.extend(binario2)
lista_operando2 = lista_operando2[::-1]

def suma(lista_operando1,lista_operando2,lista_acarreo_suma):
    if len(lista_operando1) > 8 or len(lista_operando2) > 8:
        return mensaje_formato_incorrecto
    if numeros_posibles not in lista_operando1 or numeros_posibles not in lista_operando2:
        return mensaje_formato_incorrecto
    for i in range(9):
        if lista_operando1[i] == "0" and lista_operando2[i] == "0" and lista_acarreo_suma[i] == "0":
            lista_resultado_suma.insert(i,"0")
        elif lista_operando1[i] == "1" and lista_operando2[i] == "0" and lista_acarreo_suma[i] == "0":
            lista_resultado_suma.insert(i,"1")
        elif lista_operando1[i] == "0" and lista_operando2[i] == "1" and lista_acarreo_suma[i] == "0":
            lista_resultado_suma.insert(i,"1")
        elif lista_operando1[i] == "1" and lista_operando2[i] == "1" and lista_acarreo_suma[i] == "0":
            lista_acarreo_suma[i + 1] = "1"
            lista_resultado_suma.insert(i,"0")
        elif lista_operando1[i] == "0" and lista_operando2[i] == "0" and lista_acarreo_suma[i] == "1":
            lista_resultado_suma.insert(i,"1")
        elif lista_operando1[i] == "1" and lista_operando2[i] == "0" and lista_acarreo_suma[i] == "1":
            lista_acarreo_suma[i + 1] = "1"
            lista_resultado_suma.insert(i,"0")
        elif lista_operando1[i] == "0" and lista_operando2[i] == "1" and lista_acarreo_suma[i] == "1":
            lista_acarreo_suma[i + 1] = "1"
            lista_resultado_suma.insert(i,"0")
        elif lista_operando1[i] == "1" and lista_operando2[i] == "1" and lista_acarreo_suma[i] == "1":
            lista_acarreo_suma[i + 1] = "1"
            lista_resultado_suma.insert(i,"1")
    lista_resultado_suma.reverse()
    return lista_resultado_suma

def resta(lista_operando1,lista_operando2,lista_acarreo_resta):
    if len(lista_operando1) > 8 or len(lista_operando2) > 8:
        return mensaje_formato_incorrecto
    if numeros_posibles not in lista_operando1 or numeros_posibles not in lista_operando2:
        return mensaje_formato_incorrecto
    for i in range(9):
        if lista_operando1[i] == "0" and lista_operando2[i] == "0" and lista_acarreo_resta[i] == "0":
            lista_resultado_resta.insert(i,"0")
        elif lista_operando1[i] == "1" and lista_operando2[i] == "0" and lista_acarreo_resta[i] == "0":
            lista_resultado_resta.insert(i,"1")
        elif lista_operando1[i] == "0" and lista_operando2[i] == "1" and lista_acarreo_resta[i] == "0":
            lista_acarreo_resta[i + 1] = "1"
            lista_resultado_resta.insert(i,"1")
        elif lista_operando1[i] == "1" and lista_operando2[i] == "1" and lista_acarreo_resta[i] == "0":
            lista_resultado_resta.insert(i,"0")
        elif lista_operando1[i] == "0" and lista_operando2[i] == "0" and lista_acarreo_resta[i] == "1":
            lista_resultado_resta.insert(i,"1")
        elif lista_operando1[i] == "1" and lista_operando2[i] == "0" and lista_acarreo_resta[i] == "1":
            lista_resultado_resta.insert(i,"0")
        elif lista_operando1[i] == "0" and lista_operando2[i] == "1" and lista_acarreo_resta[i] == "1":
            lista_resultado_resta.insert(i,"0")
        elif lista_operando1[i] == "1" and lista_operando2[i] == "1" and lista_acarreo_resta[i] == "1":
            lista_acarreo_resta[i + 1] = "1"
            lista_resultado_resta.insert(i,"1")
    lista_resultado_resta.reverse()
    return lista_resultado_resta

#Salida
suma_binaria:list = suma(lista_operando1,lista_operando2,lista_acarreo_suma)
resta_binaria:list = resta(lista_operando1,lista_operando2,lista_acarreo_resta)
def main():
    """Ejecuta la tarea principal del programa."""
    #Salida
    if operacion == "+":
        print(suma_binaria)
    elif operacion == "-":
        print(resta_binaria)
    else: #Asumo que si no se indica se refiere a que el usuario inserte cualquier otra cosa
        print(suma_binaria)
        print(resta_binaria)
if __name__ == "__main__":
    # Solo se ejecuta al lanzar directamente este archivo.
    main()
else:
    # El módulo también puede ser importado por otro programa.
    print("Módulo importado")