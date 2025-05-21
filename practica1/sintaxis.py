# 1. Sintaxis de Python
# Comentarios en Python
# comentarios de una sola línea

# 2. Strings
print("hola mundo soy una cadena")
print('yo soy otra')

variable1 = "hola soy una cadena"
print(len(variable1))

print(variable1[2:5])
print(variable1[2:])
print(variable1[:5])

# 3. Variables
x = int(3)
y = float(3)
z = str(3)
print(x, y, z)
print(type(x), type(y), type(z))

# 4. Solicitud de datos
a = input("Introduce cualquier dato: ")

try:
    b = int(input("Introduce un número entero: "))
    c = float(input("Introduce un número decimal: "))
    print(a, b, c)
except ValueError:
    print("Error: por favor introduce datos válidos para el número entero y el decimal.")

# 5. Boolean, comparación y operadores lógicos
print(10 > 9)
print(10 < 9)
print(10 == 9)
print(10 >= 9)
print(10 <= 9)
print(10 != 9)

x = 1
print(x < 5 and x < 10)
print(x < 5 or x < 10)
print(not (x < 5 and x < 10))
    