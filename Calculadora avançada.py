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
  helps: list[str] = ["Simbolos", "Formulas", "Calculadora", "Outro"]
  matematica = {"trignometria": ["Seno", "Cosseno", "Tangente", "ArcSeno", "ArcCosseno", "Cotangente"],
                "Equações" : ["Formula resolvente"]
                }
  print("Escolhe o tipo de ajuda: ")
  for i in range(len(helps)):
    print(i+1, helps[i])
  while True:
    ajuda: str = input().capitalize()
    if ajuda == "Simbolos" or ajuda == "1":
      print("\nTodos os simbolos:\n")
      print("O + representa adição")
      print("O * representa multiplicação")
      print("O - representa subtração")
      print("A / representa divisão")
      print("O ^ coloca o numero em expoente")
      print("A # representa raiz quadrada")
      break
    elif ajuda == "Formulas" or ajuda == "2":
      print("Escolhe a area das formulas: ")

      break
    elif ajuda == "Calculadora" or ajuda == "3":
      break
    elif ajuda == "Outro" or ajuda == "4":
      break
    else:
      print("Não encontrei a tua ajuda, tenta denovo!")

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
