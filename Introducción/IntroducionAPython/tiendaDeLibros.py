print('Proporcione los siguientes datos del libro:')
nombre = input('Proporciona el nombre:')
id = int(input('Proporciona el ID:'))
precio = float(input('Proporciona el precio:'))
envio = input('Indica si el libro es gratuito (True/False):')

if envio == "True":
    envio = True
elif envio == "False":
    envio = False
else:
    envio = 'Valor incorrecto, debe ser True/False'
    
print('Nombre: ', nombre)
print('ID: ', id)
print('Precio: $', precio)
print('Envío gratuito: ', envio)
print(type(envio))