import time
import random
from load import load
from calchelp import calc_help

def main():
  load() #inicia a calculadora
  while True: #pede os calculos sempre(fica no loop)
    try:
      calculo = input()
      if calculo == "stop": #se for "stop" então desliga a calculadora
        powerOff()
        break
      elif calculo == "help": #se for "help" abre o menu de ajudas
        calc_help()
        continue
      resultado = matematica(calculo) #caso não seja esses dois casos, ele faz a conta
      print(resultado)
      
    except ValueError:
      print("Syntax Error") #Não faz a conta se houver um erro ou se dividirmos algo por 0
    except ZeroDivisionError as e:
          print(e)

def matematica(n):            #Função que faz a matematica
  for operator in "+-*/^#":
        index = n.find(operator)  #procura o operador
        if index != -1:          
            if operator == "#":   #primeiro testa de é raiz quadrada
               numero = n[index+1:]
               return float(numero) ** 0.5 
            numero = n[:index]              #divide os numeros pelos operadores
            resto = n[index + 1:]
            
            numero_resto = matematica(resto)  #faz a recursividade
            
            if operator == "+":
                return float(numero) + numero_resto     #Faz as contas finais
            elif operator == "-":
                return float(numero) - numero_resto
            elif operator == "*":
                return float(numero) * numero_resto
            elif operator == "/":
                if float(numero_resto) == 0:
                    raise ZeroDivisionError("Math Error") #verifica se não divide por 0
                return float(numero) / numero_resto
            elif operator == "^":
              return float(numero) ** numero_resto

  return float(n) #caso não hava operador ou as contas acabem ele retorna o valor

def powerOff(): #função para desligar
  print("Turning Off")
  for i in range(3):
    time.sleep(0.2)   #apenas uns textos para fingir que está a desligar
    print("...")
  print("Power Off :)")

main()

#chama a função para começar a calculadora
