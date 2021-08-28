calificacion = float(input('Introduzca calificación: '))

def calcula_calificacion(calificacion):
        try:
                if float(calificacion) >= 10.0:
                        print('Introduzca un número valido')
                elif float(calificacion) >= 0.9:
                        print('Sobresaliente')
                elif float(calificacion) >= 0.8:
                        print('Notable')
                elif float(calificacion) >= 0.7:
                        print('Bien')
                elif float(calificacion) >= 0.6:
                        print('Suficiente')
                elif float(calificacion) <= 0.6:
                        print('Insuficiente')
                
        except:
                print('Introduzca un número valido')
calcula_calificacion(calificacion)