from decimal import Decimal
import math
# Ejercicio 1: Crear una lista, una tupla, un flotante (float), un entero (integer), un decimal  y un diccionario.
mi_lista = ['manzana', 'banana', 'cereza']
mi_tupla = ('rojo', 'verde', 'azul')
mi_float = 7.34
mi_integer = 42
mi_decimal = Decimal ('10.50')
mi_diccionario = {'nombre': 'Ana', 'edad': 28, 'ciudad': 'Madrid'}

# Ejercicio 2: Redondea tu flotante (float) hacia arriba.
float_redondeado:float = math.ceil(mi_float)

# Ejercicio 3: Obtén la raíz cuadrada de tu flotante (float).
raiz_cuadrada = math.sqrt(mi_float)

# Ejercicio 4: Selecciona el primer elemento de tu diccionario.
primer_elemento_dict = mi_diccionario['nombre']

# Ejercicio 5: Selecciona el segundo elemento de tu tupla.
segundo_elemento_tupla = mi_tupla[1]

# Ejercicio 6: Añade un elemento al final de tu lista.
mi_lista.append('pera')

# Ejercicio 7: Reemplaza el primer elemento de tu lista.
mi_lista[0] = 'kiwi'

# Ejercicio 8: Ordena tu lista alfabéticamente.
mi_lista.sort()

# Ejercicio 9: Usa la reasignación para añadir un elemento a tu tupla.
mi_tupla = mi_tupla + ('amarillo',)

# --- Comprobación de Resultados en Pantalla ---
print(f"Ej 1 (Decimal): {mi_decimal}")
print(f"Ej 2 (Redondeo hacia arriba): {float_redondeado}")
print(f"Ej 3 (Raíz cuadrada): {raiz_cuadrada: 4f}")
print(f"Ej 4 (Primer elemento dict): {primer_elemento_dict}")
print(f"Ej 5 (Segundo elemento tupla): {segundo_elemento_tupla}")
print(f"Ej 6,7 y 8 (Lista con nuevo elemento): {mi_lista}")
print(f"Ej 9 (Tupla con nuevo elemento): {mi_tupla}")