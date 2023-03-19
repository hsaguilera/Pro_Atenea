# El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 192. Este valor corresponde a la jornada laboral establecida en el contrato (48 horas a la semana y 4 semanas al mes). 
# Las horas extras se liquidan con un recargo del 25% sobre el valor de una hora normal
# Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 5% del salario base
# El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras, más las bonificaciones (si las hay)
# Se descontará 3.5% del salario total antes de descuentos para el plan obligatorio de salud
# Se descontará 4% del salario total antes de descuentos para el aporte a pensión
# Se descontará 1% del salario total antes de descuentos para caja de compensación.

# Se recibe salario base, horas extras y bonificaciones (1 si hay, 0 no hay) 
sal_base, hor_extra, bon = input ().split() #Split permite la entrada de datos por espacios, pog
sal_base = float (sal_base)
hor_extra = int (hor_extra)
bon = int (bon)

#print (sal_base, "El tipo de dato", type (sal_base))
#print (hor_extra, "El tipo de dato", type (hor_extra))
#print (bon, "El tipo de dato", type (bon))

valor_hora = sal_base/192
valor_hora_ext = valor_hora * 1.25
val_bon = sal_base * 0.05
sal_total = (sal_base) + (valor_hora_ext * hor_extra) + (val_bon * bon)
salario = (sal_total - ((sal_total * 0.035) + (sal_total * 0.04) + (sal_total * 0.01)))
print ((float (round (salario, 1))))