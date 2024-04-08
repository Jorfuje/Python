""" condicion = 10

if condicion == True:
    print('La condición es verdadera!')
elif condicion == False:
    print('La condición es falsa!')
else:
    print('La condición no reconocida!')
    
    
numero = int(input('"Proporciona un número entre 1 y 3: '))

if numero == 1:
    numeroTexto = 'Número uno'
elif numero == 2:
    numeroTexto = 'Número dos'
elif numero == 3:
    numeroTexto = 'Número tres'
else:
    numeroTexto = 'Valor fuera de rango'
    
print('Número proporcionado: ' + numeroTexto) """


# Condición terniaria
condicion = False

print('Condición verdadera') if condicion else print('Condición false')

# Es equivalente a:
if condicion == True:
    print('La condición es verdadera!')
elif condicion == False:
    print('La condición es falsa!')
else:
    print('La condición no reconocida!')