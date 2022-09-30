class Vehiculo:

    color = ''
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):

    velocidad = 0;
    cilindrada = 0;

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Coche: color: {self.color}, ruedas: {self.ruedas}, puertas: {self.puertas}, velocidad: {self.velocidad}, cilindrada: {self.cilindrada}"


coche1 = Coche('Amarillo', 4, 6, 360, 2000);
print(coche1.__str__())

