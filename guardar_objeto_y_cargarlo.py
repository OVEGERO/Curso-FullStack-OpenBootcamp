import pickle

class Vehiculo:
    marca = ''
    color = ''
    anio = 0

    def __init__(self, marca, color, anio):
        self.marca = marca
        self.color = color
        self.anio = anio

    def __str__(self):
        return 'Marca: ' + self.marca + ', Color: ' + self.color + ', Año: ' + str(self.anio)


vehiculo = Vehiculo('Ford', 'Rojo', 2018)

f = open('vehiculo.bin', 'wb')

pickle.dump(vehiculo, f)

f.close()

f = open('vehiculo.bin', 'rb')

vehiculo = pickle.load(f)

print(vehiculo)

f.close()
