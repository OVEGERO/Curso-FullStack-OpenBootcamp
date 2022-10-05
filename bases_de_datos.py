import sqlite3

conn = sqlite3.connect('ejemplo.db')

cursor = conn.cursor()

cursor.execute('''DROP TABLE alumnos''')

cursor.execute('''CREATE TABLE alumnos (id INTEGER PRIMARY KEY, nombre TEXT, 
apellido TEXT)''')

cursor.execute('''INSERT INTO alumnos VALUES (1, 'Alexis', 'Sánchez')''')
cursor.execute('''INSERT INTO alumnos VALUES (2, 'Johann', 'Vázquez')''')
cursor.execute('''INSERT INTO alumnos VALUES (3, 'Alfred', 'Sanh')''')
cursor.execute('''INSERT INTO alumnos VALUES (4, 'Jorge', 'González')''')
cursor.execute('''INSERT INTO alumnos VALUES (5, 'Dante', 'Arely')''')
cursor.execute('''INSERT INTO alumnos VALUES (6, 'Virgilio', 'Tarrega')''')
cursor.execute('''INSERT INTO alumnos VALUES (7, 'Hannah', 'Barros')''')
cursor.execute('''INSERT INTO alumnos VALUES (8, 'Rodrigo', 'Vidovic')''')

conn.commit()

cursor.execute('''SELECT nombre, apellido FROM alumnos WHERE id=1''')
print(cursor.fetchone())

conn.close()




