def anioBisiesto(anio):

    if( anio%400 == 0 or (anio % 4 == 0 and not (anio % 100 == 0)) ):
        print(f'El año {anio} es un año bisiesto')
    else:
        print(f'El año {anio} no es un año bisiesto')

anioBisiesto(1900)