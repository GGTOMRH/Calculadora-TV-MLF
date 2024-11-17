import time
import random

def main():
  load()
  while True:
    try:
      calculo = input()
      if calculo == "stop":
        break
      elif calculo == "help":
        calc_help()
        continue
      resultado = matematica(calculo)
      print(resultado)
    except ValueError:
      print("Syntax Error")
    except ZeroDivisionError as e:
          print(e)

def load():
  print("A inciar calculadora TV-MLF")
  time.sleep(0.5)
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
  time.sleep(0.5)
  print("Bem-vindo à TV-MLF :) ")

def calc_help():
  print("Escolhe o tipo de ajuda: ")


def matematica(n):
  for operator in "+-*/^":
        index = n.find(operator)
        if index != -1:
            numero = n[:index]
            resto = n[index + 1:]
            
            numero_resto = matematica(resto)
            
            if operator == "+":
                return float(numero) + numero_resto
            elif operator == "-":
                return float(numero) - numero_resto
            elif operator == "*":
                return float(numero) * numero_resto
            elif operator == "/":
                if float(numero_resto) == 0:
                    raise ZeroDivisionError("Math Error")
                return float(numero) / numero_resto
            elif operator == "^":
              return float(numero) ** numero_resto

  return float(n)

main()