frase = input('introduce una frase: ')
frase.lower()
letra = input('introduce una letra a buscar: ')
print(f'la letra {letra} se repite {frase.count(letra)}')
lista = frase.split()
print(f'la cantidad de palabras en tu frase es: {len(lista)}')
print(f'la primera letra es: {frase[0]} y la ultima es: {frase[-1]}')
print(f'frase al revez:\n{frase[::-1]}')
print('La palabra python esta en la frase') if frase.find('python') else print('la palabra python no esta en la frase')


