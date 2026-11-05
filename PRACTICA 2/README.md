# Nombre, Apellidos y fecha

Marcos Martin Reinon, 05/11/2026

# Práctica 2 - Palíndromo binario

El alumnado programará en Python un script que recibe una cadena binaria por la terminal e indica si es un palíndromo.

## Objetivos de aprendizaje

- Recibir y tratar datos pasados como argumentos desde la línea de comandos.
- Validar la entrada del usuario y gestionar los casos de error.
- Aplicar un algoritmo de comparación sobre cadenas de longitud arbitraria.
- Devolver códigos de salida adecuados al terminar el programa.

## Descripción

Desarrolla un programa llamado `palindromo.py` que reciba **una cadena por argumento** al ejecutarlo desde la terminal y determine si es un **palíndromo**, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda.

La cadena puede tener **cualquier longitud** y solo puede estar formada por los caracteres `0` y `1`.

### Forma de ejecución

```bash
python palindromo.py <cadena>

python palindromo.py 1221
# Salida: Es un palindromo

python palindromo.py 123
# Salida (por stderr): formato incorrecto

python palindromo.py
# Salida (por stderr): número de argumentos no válido
```
