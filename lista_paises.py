paises = ''
paises_set = {''}
paises_separados = ['']

print('Introduce los países que quieras seguidos con una coma (,): ')
paises = input()

paises_separados = paises.lower().title().split(',')
paises_separados.sort()
paises_separados = map(lambda x: x.strip(), paises_separados)

paises_set = set(paises_separados)

print(list(paises_set))

