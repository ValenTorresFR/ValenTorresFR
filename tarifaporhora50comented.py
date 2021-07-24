horas = input('Cuantas horas trabaja su empleado por jornada?: ')                                                   # Este codigo fue realizado por Valentín Torres Porcel el día 24/7/2021 (Venticuatro de Julio de 2021)  
tarifa  = input('Cuál es la tarifa por hora?: ')
pregunta = input('Desea aumentar la tarifa pasada determinada cantidad de horas?: ')
cuandoau = input('En que cantidad de horas empieza a aumentar la tarifa?: ')
aumento = input('Cuantas veces aumenta la tarifa luego de superar esa cantidad de horas?: ')
salario = float(horas)*float(tarifa)


if float(horas) > float(cuandoau):                                                                                  # Si la cantidad de horas supera las 40 horas:
        resto = float(horas) - float(cuandoau)                                                                      #   Calcular el excedente de horas restando la cantidad de horas trabajadas menos 40
        mult = float(resto)*float(aumento)                                                                          #   Multiplicar dicho excedente por la cantidad de veces que se desea pagar al empleado por las horas excedidas de 40, en este caso, 1.5 veces por cada horas excedida de 40 horas.
        n_salario = float(salario) - (float(resto)*float(tarifa))                                                   #   Restar del salario, la multiplicación del resto excedido por la tarifa por hora. Esto se hace para no sumar las horas execedidas al pago de las horas que no exceden las 40 horas.
        nuevo_sum = float(mult)*float(tarifa)                                                                       #   Luego de saber la variante 'mult' (cuanto valen las horas excedidas), se multiplica 'mult' por la tarifa que se le pagan a todas las horas (sin contar si son normales o excedidas).
        nuevo_salario = float(nuevo_sum)+float(n_salario)                                                           #   Determinamos que el nuevo salario de nuestro empleado es la suma del valor monetario de nuestro excedente (la variable 'nueva_sum') mas las horas normales del salario multiplicadas por la tarida.
        print(f"El salario es: USD {round(nuevo_salario, 2)} por jornada")                                          #   Imprimimos en pantalla el valor de nuestro nuevo salario.

else:                                                                                                               # Si la cantidad de horas NO supera las 40 horas:
    print(f"El salario es: USD {round(salario, 2)} por jornada")                                                    #   Imprimimos en pantalla el valor de nuestro salario (horas por tarifa).
