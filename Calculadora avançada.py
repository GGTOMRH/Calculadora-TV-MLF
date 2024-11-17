import time
import random

def matematica(n):
  for operator in "+-*/^":
        index = n.find(operator)
        if index != -1:
            numero = n[:index]
            resto = n[index + 1:]
            
            numero_resto = matematica(resto)
            
            if operator == "+":
                return int(numero) + numero_resto
            elif operator == "-":
                return int(numero) - numero_resto
            elif operator == "*":
                return int(numero) * numero_resto
            elif operator == "/":
                if int(numero_resto) == 0:
                    raise ZeroDivisionError("Math Error")
                return int(numero) // numero_resto
            elif operator == "^":
              return int(numero) ** numero_resto

  return int(n)

#iniciar a calculador
print("A inciar calculadora TV-MLF")
load = 0
while load < 100:
  if load > 95:
    load += 1
  elif load > 90:
    load += random.randint(1, 5)
  else:
    load += random.randint(5, 10)
  print("loading", str(load)+"%")
  time.sleep(0.1)
print("Bem-vindo à TV-MLF :) ")

#input da conta
while True:
  try:
    calculo = input()
    if calculo == "stop":
      break
    if calculo == "help":
      print("")
    matematica(calculo)
    resultado = matematica(calculo)
    print(resultado)
  except ValueError:
    print("Syntax Error")
  except ZeroDivisionError as e:
        print(e)