def tablamultiplicar(numero):

  for i in range(1, 11):
      resultado = numero * i
      print(f"{numero} * {i} = {resultado}")
    
def operaciones():
  numero1 = float(input("Ingrese el primer número: "))
  numero2 = float(input("Ingrese el segundo número: "))
  operacion = input("Ingrese la operación a realizar (suma, resta, division): ")

  if operacion == 'suma':
      return numero1 + numero2
  elif operacion == 'resta':
      return numero1 - numero2
  elif operacion == 'division':
      if numero2 != 0:
          return numero1 / numero2
      else:
          return "Error: No se puede dividir entre cero."
  else:
      return "Operación no válida"

def area_cuadrado(lado):
  return lado * lado

numero_tabla = int(input("Ingresa el número para la tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero_tabla}:")
tablamultiplicar(numero_tabla)

print("Operaciones:")
resultado_operacion = operaciones()
print("Resultado:", resultado_operacion)

lado_cuadrado = float(input("Ingrese el lado del cuadrado para calcular su área: "))
print("Área del cuadrado:", area_cuadrado(lado_cuadrado))