a = 3
b = 2

""" Todos los operadores de comparación
    regresan un valor de tipo Boolenao """
    
resultado = a == b # Comparar la iguldad
print(resultado)

resultado = a != b # Comparar la diferencia
print(resultado)

resultado = a > b # Comparar la a mayor que b
print(resultado)

resultado = a >= b # Comparar la a mayor o igual que b
print(resultado)

resultado = a < b # Comparar la a menor que b
print(resultado)

resultado = a <= b # Comparar la a menor o igual que b
print(resultado)

if(b % 2 == 0):
    print('Es par')
else:
    print('Es impar')
    
edadLimite = 18

edadPersona = 20

if(edadPersona > edadLimite):
    print('Es un adulto')
else:
    print('Es menor de edad')
