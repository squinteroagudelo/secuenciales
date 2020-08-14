# Ejercicio 1

inversion = float(input('Ingrese el valor de su inversión: $ '))
ganancia = inversion * 0.02
print(f'Su ganancia es de $ {ganancia}.')

# Ejercicio 2

basico = float(input('Ingrese el salario básico: $ '))
venta1 = float(input('Ingrese el valor de la primera venta: $ '))
venta2 = float(input('Ingrese el valor de la segunda venta: $ '))
venta3 = float(input('Ingrese el valor de la tercera venta: $ '))

comision = (venta1 + venta2 + venta3) * 0.1
total = basico + comision

print(f'La comisión por las venta es $ {comision} y el sueldo neto es $ {total}')

# Ejercicio 3

valor_compra = float(input('Ingrese el valor de la compra: $ '))
total_pagar = valor_compra - valor_compra * 0.15
print(f'El total a pagar es $ {total_pagar}')

# Ejercicio 4

nota_1 = float(input('Ingrese el la nota 1: '))
nota_2 = float(input('Ingrese el la nota 2: '))
nota_3 = float(input('Ingrese el la nota 3: '))
examen = float(input('Ingrese la nota del examen: '))
trabajo = float(input('Ingrese la nota del trabajo final: '))

promedio = (nota_1 + nota_2 + nota_3) / 3
final = promedio * 0.55 + examen * 0.3 + trabajo * 0.15
print(f'La calificación final es {final:.2f}')

# Ejercicio 5

hombres = int(input('Ingrese la cantidad de hombres: '))
mujeres = int(input('Ingrese la cantidad de mujeres: '))

porc_homb = (hombres * 100) / (hombres + mujeres)
porc_muj = (mujeres * 100) / (hombres + mujeres)

print(f'El porcentaje de hombre del grupo es {porc_homb}% y el de mujeres {porc_muj}%')

# Ejercicio 6

from datetime import date

def calcular_edad(nac):
    actual = date.today()
    edad = actual.year - nac.year
    edad -= ((actual.month, actual.day) < (nac.month, nac.day))
    return edad

nac = date(1990, 6, 18)
edad = calcular_edad(nac)

print(f"Tu edad es {edad} años")
