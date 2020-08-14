# Ejercicio 1

pesos = float(input('Ingrese la cantidad en pesos: $ '))
unidad_cambiaria = float(input('Ingrese el valor de la unidad cambiaria: '))
dolares = pesos * unidad_cambiaria

print(f'{pesos} COP equivalen a {dolares} USD')

# Ejercicio 2

numero = float(input('Digite un número: '))
absoluto = abs(numero)
print(f'El valor absoluto de {numero} es {absoluto}')

# Ejercicio 3

presion = float(input('Ingrese la presión: '))
volumen = float(input('Ingrese el voliumen: '))
temperatura = float(input('Ingrese la temperatura: '))

masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f'La masa calculada es {masa:.2f}')

# Ejercicio 4

edad = int(input('Ingrese la edad: '))
pulsaciones = (220 - edad) / 10

print('La cantidad de pulsaciones por cada 10 s que una persona de {} años debe tener es de {}'.format(edad, pulsaciones))

# Ejercicio 5

salario = float(input('Ingrese su salario: $ '))
incremento = salario * 0.25
salario += incremento
print('Su nuevo salario es de $ {}'.format(salario))

# Ejercicio 6

presupuesto = float(input('Ingrese el presupuesto anual del hospital: $ '))
ginecologia = presupuesto * 0.4
traumatologia = presupuesto * 0.3

print(f'El área de ginecología obtiene $ {ginecologia} del presupuesto anual, mientras que traumatología y pediatria obtienen $ {traumatologia}')

# Ejercicio 7

precio_compra = float(input('Ingrese el precio de compra del artículo: $ '))
aumento_requerido = precio_compra * 0.3
precio_venta = precio_compra + aumento_requerido

print('Para obtener una ganancia del 30%, el artículo debe ser vendido en $ {}'.format(precio_venta))

# Ejercicio 8

lunes = float(input("Ingrese el tiempo en minutos obtenido el Lunes: "))
miercoles = float(input('Ingrese el tiempo en minutos obtenido el Miércoles: '))
viernes = float(input('Ingrese el tiempo en minutos obtenido el Viernes: '))

promedio = (lunes + miercoles + viernes) / 3

print('La persona tarda en promedio {} minutos'.format(promedio))

# Ejercicio 10

examen_mat = float(input('Digite la nota del examen de matemáticas: '))
tarea_1_mat = float(input('Digite la nota de la tarea 1 de matemáticas: '))
tarea_2_mat = float(input('Digite la nota de la tarea 2 de matemáticas: '))
tarea_3_mat = float(input('Digite la nota de la tarea 3 de matemáticas: '))
matematicas = (examen_mat * 0.9) + ((tarea_1_mat + tarea_2_mat + tarea_3_mat)/3) * 0.1

examen_fis = float(input('Digite la nota del examen de física: '))
tarea_1_fis = float(input('Digite la nota de la tarea 1 de física: '))
tarea_2_fis = float(input('Digite la nota de la tarea 2 de física: '))
fisica = (examen_fis * 0.8) + ((tarea_1_fis + tarea_2_fis)/2) * 0.2

examen_qui = float(input('Digite la nota del examen de química: '))
tarea_1_qui = float(input('Digite la nota de la tarea 1 de química: '))
tarea_2_qui = float(input('Digite la nota de la tarea 2 de química: '))
tarea_3_qui = float(input('Digite la nota de la tarea 3 de química: '))
quimica = (examen_qui * 0.85) + ((tarea_1_qui + tarea_2_qui + tarea_3_qui)/3) * 0.15

prom_general = (matematicas + fisica + quimica) / 3

print(f'El promedio general del alumno es {prom_general:.2f}\nMatemáticas: {matematicas:.2f}\nFísica: {fisica:.2f}\nQuímica: {quimica:.2f}')