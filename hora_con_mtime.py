import time

hora_actual = time.localtime()
print("Hora actual: ", hora_actual.tm_hour, ":", hora_actual.tm_min, ":", hora_actual.tm_sec)
if hora_actual.tm_hour >= 19:
    print("Fin de la jornada laboral")
else:
    if (19 - hora_actual.tm_hour) == 1:
        hora_salida = 0
    else:
        hora_salida = (19 - hora_actual.tm_hour)
    minutos_salida = 60 - hora_actual.tm_min
    segundos_salida = 60 - hora_actual.tm_sec
    print(
        f"Faltan {hora_salida} horas {minutos_salida} minutos {segundos_salida} segundos para terminar la jornada laboral")
