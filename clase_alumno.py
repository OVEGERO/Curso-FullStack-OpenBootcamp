class Alumno:

    nombre = ''
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_nombre(self):
        return f'El alumno se llama {self.nombre}'

    def imprimir_nota(self):
        return f'La nota del alumno es {self.nota}'

    def is_aprobado(self):
        if self.nota >= 7:
            return True
        return False

    def __str__(self):
        return f'El alumno {self.nombre} tiene una nota de {self.nota}'


alumno1 = Alumno('Dante Emilio Gaviria Alliguieri', 5)
print(alumno1.imprimir_nombre())
print(alumno1.imprimir_nota())
print('El alumno está aprobado:', alumno1.is_aprobado())
print(alumno1.__str__())
