# 1.Sintaxis de Python
# Comentarios en Python
# comentarios de una sola linea 

#2. strings
print("hola mundo soy una cadena")
print('yo soy otra')

variable1="hola soy una cadena"
print(len(variable1))

print(variable1[2:5])
print(variable1[2:])
print(variable1[:5])

#3.Variables

x=int(3)
y=float(3)
z=str(3)
print(x,y,z)
print(type(x),type(y),type(z))

#4.Solicitud de datos

a= input("introduce cualquier dato")

b= int(input("introduce un numero entero"))

c= float(input("introduce un numero decimal"))

print(a,b,c)

#4. boolean,comparacion y operadores logicos

print(10>9)
print(10<9)
print(10==9)
print(10>=9)
print(10<=9)
print(10!=9)

x= 1
print(x<5 and x<10)
print(x<5 or x<10)
print(not(x<5 and x<10))