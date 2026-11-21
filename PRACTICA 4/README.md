# Cifrado Rail Fence (Transposición en Zigzag)

Este proyecto es una implementación en Python del algoritmo de cifrado **Rail Fence** (o cifrado por transposición en riel) configurado para trabajar con **3 raíles** (filas).

**Nombre:** Marcos Martín Reinon  
**Lenguaje:** Python 3  

---

## 📋 ¿Qué hace este programa?

El programa recibe una cadena de texto desde la línea de comandos, elimina los espacios en blanco, valida que los caracteres pertenezcan al alfabeto español (incluyendo la letra `Ñ`) y genera el texto cifrado ordenando las letras en un patrón en zigzag a lo largo de 3 raíles.

---

## ⚙️ ¿Cómo funciona el cifrado Rail Fence?

El cifrado Rail Fence es un tipo de cifrado por transposición. En lugar de sustituir unas letras por otras, reorganiza las letras del mensaje original siguiendo una estructura en zigzag sobre un número determinado de raíles o líneas paralelas.

### Algoritmo de 3 Raíles

Para una cadena de texto, el programa distribuye cíclicamente las letras entre 3 listas/raíles siguiendo una secuencia de movimiento hacia abajo y hacia arriba ($1 \rightarrow 2 \rightarrow 3 \rightarrow 2 \rightarrow 1 \dots$):

1. **Riel 1:** Recibe la 1.ª letra, la 5.ª, la 9.ª, etc. (índices con patrón $4k + 1$).
2. **Riel 2:** Recibe la 2.ª, 4.ª, 6.ª, 8.ª letra, etc. (índices pares).
3. **Riel 3:** Recibe la 3.ª, 7.ª, 11.ª letra, etc. (índices con patrón $4k + 3$).

Finalmente, el texto cifrado se obtiene concatenando las letras del **Riel 1** + **Riel 2** + **Riel 3**.

---

## 🚀 Requisitos y Ejecución

### Requisitos
* Python 3.x instalado.

### Cómo ejecutar el programa

El programa requiere pasar la frase entre comillas como argumento por la línea de comandos:

```bash
python railfence.py "TU FRASE A CIFRAR"
```

> **Nota de Validación:**
> * El programa acepta únicamente letras de la A a la Z (incluyendo la Ñ) y espacios.
> * Las minúsculas se convierten automáticamente a mayúsculas.
> * Los espacios se eliminan antes de procesar el cifrado.

---

## 💡 Ejemplos de uso

### Ejemplo 1: "HOLA MUNDO"

Al ejecutar:
```bash
python railfence.py "HOLA MUNDO"
```

1. **Preprocesamiento:** Se limpian los espacios y se convierte a mayúsculas $\rightarrow$ `HOLAMUNDO` (9 letras).
2. **Distribución en zigzag (3 raíles):**

```text
Riel 1: H . . . M . . . O
Riel 2: . O . A . U . D .
Riel 3: . . L . . . N . .
```

3. **Lectura horizontal por filas:**
   * **Fila 1:** `HMO`
   * **Fila 2:** `OAUD`
   * **Fila 3:** `LN`

4. **Salida resultante:**
```text
HMOOAUDLN
```

---

### Ejemplo 2: "CIFRADO DE RAIL"

Al ejecutar:
```bash
python railfence.py "CIFRADO DE RAIL"
```

1. **Preprocesamiento:** `CIFRADODERAIL`
2. **Distribución:**
```text
Riel 1: C . . . A . . . E . . . L
Riel 2: . I . R . D . D . R . I .
Riel 3: . . F . . . O . . . A . .
```
3. **Salida resultante:**
```text
CAELIRDDRIFOA
```

---

## ⚠️ Manejo de Errores

* **Argumentos insuficientes o excesivos:** Si no se pasa una cadena o se pasan múltiples parámetros sin comillas, mostrará un mensaje de error por la salida estándar de errores (`sys.stderr`).
* **Caracteres no válidos:** Si el texto contiene números, símbolos o caracteres especiales (fuera del alfabeto A-Z, Ñ y espacio), el programa lanzará un `ValueError("Formato incorrecto")`.