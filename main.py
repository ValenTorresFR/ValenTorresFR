horas = input('Cuantas horas trabaja su empleado: ')                                                         # Este codigo fue realizado por Valentín Torres Porcel el día 28/8/2021 (Ventiocho de Agosto de 2021)  
tarifa  = input('Cuál es la tarifa por hora?: ')

def calculo_salario(horas, tarifa):

        salario = float(horas)*float(tarifa)                                                                                                  
        cuandoau = float(40)                                       
        aumento = float(1.5)
        if float(horas) > float(cuandoau):
                try:                                                                                                     
                        resto = float(horas) - float(cuandoau)                                                                      
                        mult = float(resto)*float(aumento)
                        n_salario = float(salario) - (float(resto)*float(tarifa))                                                   
                        nuevo_sum = float(mult)*float(tarifa)                    
                        salario_jornada = float(nuevo_sum)+float(n_salario)                                                                                                                                                                                                                                                                                                                                                  
                        print(f"El salario es: USD {round(salario_jornada, 2)}")
                except:
                        print('Error')   
        else:
                try:
                        print(f"El salario es: USD {round(salario_jornada, 2)}")
                except:
                        print('Error') 

calculo_salario(horas, tarifa)
