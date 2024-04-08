""" a = 3
valorMinimo = 0
valorMaximo = 5
dentroRango = a >= valorMinimo and a <= valorMaximo # Operador lógico y (and)
# print(dentroRango)
if(dentroRango):
    print('Dentro del rango!')
else:
    print('Fuera del rango!') """
    

vacaciones = False
diaDescanso = False

if(vacaciones or diaDescanso): # Operador lógico o (or)
    print('Puedes ir de paseo!')
else:
    print('Tienes deberes!')

print(not(vacaciones)) # Operador lógico no (not), invertir el valor