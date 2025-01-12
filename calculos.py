import math as m

pi = m.pi

formulasFundamentais = ["Seno", "Cosseno", "Tangente"]


def teorema_de_pitagoras():
  x = input("Primeiro cateto: ")
  y = input("Segundo cateto: ")
  h = (float(x) ** 2 + float(y) ** 2) ** 0.5
  print(f"A hipotenusa é {h}")

def distancia():
  x1 = input("X do primeiro ponto:")
  y1 = input("Y do primeiro ponto:")
  x2 = input("X do segundo ponto:")
  y2 = input("Y do segundo ponto:")
  distancia = m.sqrt(((float(x1) - float(x2))**2) + ((float(y1) - float(y2))**2))
  print(f"A distancia entre os pontos é {distancia}")

def formulas_fundamentais():
  print("Escolhe uma razão trignometrica:")
  for i, formula in enumerate(formulasFundamentais, start=1):
    print(f"{i}. {formula}")
    
  while True:
      y = input()
      if y == "1" or y == "Seno":
        seno = input("Qual é o seno?:")
        cos = m.sqrt(1 - (float(seno) ** 2))
        tg = float(seno)/float(cos)
        print(f"Cosseno:{cos}\nTangente:{tg}")
        break
      elif y == "2" or y == "Cosseno":
        cos = input("Qual é o cosseno?:")
        seno = m.sqrt(1 - (float(cos) ** 2))
        tg = float(seno)/float(cos)
        print(f"Seno:{seno}\nTangente:{tg}")
        break
      elif y == "3" or y == "Tangente":
        tg = input("Qual é a tangente?:")
        cos = m.sqrt(1/((float(tg) ** 2) + 1))
        sen = float(tg) * float(cos)
        print(f"Cosseno:{cos}\nSeno:{sen}")
        break
      else:
        print("Não encontrei essa razão trignometrica! tenta denovo.")

def seno():
  alpha = input("Angulo em rad: ")
  if alpha != "pi":
    sen = m.sin(m.radians(float(alpha)))
    print(round(sen, 4))
  else:
    print(0)

def cosseno():
  alpha = input("Angulo em rad: ")
  if alpha != "pi":
    cos = m.cos(m.radians(float(alpha)))
    print(round(cos, 4))
  else:
    print(1)

def tangente():
  alpha = input("Angulo em graus: ")
  if alpha != "pi":
    tg = m.tan(m.radians(float(alpha)))
    print(round(tg, 4))
  else:
    print(0)

def frequencia():
  x = input("Qual é o periodo?")
  f = 1 / float(x)
  print(f"A frequencia é {f}")

def periodo():
  x = input("Qual é a frequencia?")
  t = 1 / float(x)
  print(f"O periodo é {t}")

def velocidade_angular():
  while True:
    escolha = input("Utilizar frquencia ou o periodo?(f/t)")
    if escolha == "f":
      f = input("Qual é a frequencia?")
      w = 2 * pi * float(f)
      break
    elif escolha == "t":
      t = input("Qual é o periodo?")
      w = 2 * pi / float(t)
      break
    else:
      print("Syntax Error. Tenta denovo")
  print(f"A velocidade angular é {w}")

def velocidade_onda():
  while True:
    lamda = input("Qual é o comprimento de onda?")
    escolha = input("Utilizar frquencia ou o periodo?(f/t)")
    if escolha == "f":
      f = input("Qual é a frequencia?")
      v = float(lamda) * float(f)
      break
    elif escolha == "t":
      t = input("Qual é o periodo?")
      v = float(lamda) / float(t)
      break
    else:
      print("Syntax Error. Tenta denovo")
  print(f"A velocidade angular é {v}")
