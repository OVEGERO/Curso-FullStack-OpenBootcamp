from functools import reduce

contador_numeros = int(input("¿Cuántos números quieres introducir? "))
lista_numeros = []

for i in range(contador_numeros):
    lista_numeros.append(int(input(f'Introduce un número ({i + 1}/{contador_numeros}): ')))

lista_numeros = filter(lambda x: x % 2 == 0, lista_numeros)
resultado = reduce(lambda x, y: x + y, lista_numeros)

print(f'La sumatoria de todos los números pares es: {resultado}')

