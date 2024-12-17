import time
import random
from load import load
from calchelp import calc_help

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

def matematica(n):
  for operator in "+-*/^#":
        index = n.find(operator)
        if index != -1:
            if operator == "#":
               numero = n[index+1:]
               return float(numero) ** 0.5 
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