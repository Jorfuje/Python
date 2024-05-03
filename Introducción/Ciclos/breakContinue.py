# Imprimir las letras a
""" for letra in "Holanda":
    if letra == "a":
        print(letra)
        break                           # Rompe todo el ciclo for
else:
    print("Fin del ciclo for") """

# Imprimir los números pares
""" for i in range(6):
    if i % 2 == 0:
        print(i) """
        
for i in range(6):
    if i % 2 != 0:
        continue                            # Continue con la siguiente iteración
    print(i)