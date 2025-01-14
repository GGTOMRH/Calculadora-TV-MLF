import math as m

pi = m.pi

formulasFundamentais = ["Seno", "Cosseno", "Tangente"]


#GEOMETRIA

def teorema_de_pitagoras():
  x = input("Primeiro cateto: ")
  y = input("Segundo cateto: ")
  h = (float(x) ** 2 + float(y) ** 2) ** 0.5
  print(f"A hipotenusa é {h}")

def teorema_de_pitagoras_oposto():
  x = input("Hipotenusa: ")
  y = input("Cateto: ")
  h = ((float(x) ** 2) - (float(y) ** 2)) ** 0.5
  print(f"O outro cateto é {h}")

def distancia():
  x1 = input("X do primeiro ponto:")
  y1 = input("Y do primeiro ponto:")
  x2 = input("X do segundo ponto:")
  y2 = input("Y do segundo ponto:")
  distancia = m.sqrt(((float(x1) - float(x2))**2) + ((float(y1) - float(y2))**2))
  print(f"A distancia entre os pontos é {distancia}")


#TRIGNOMETRIA

def radian_degrees():
  print("1. Radianos --> Graus\n2. Graus --> Radianos")
  while True:
    escolher = input()
    if escolher == "1":
      angulo = input("Qual é o ângulo em radianos?:")
      anguloG = float(angulo) * (180 / m.pi)
      print(f"O ângulo em graus é {anguloG}")
      break
    elif escolher == "2":
      angulo = input("Qual é o ângulo em graus?:")
      anguloR = float(angulo) * (m.pi / 180)
      print(f"O ângulo em graus é {anguloR}")
      break
    else:
      print("Não encontrei essa escolha! Tenta denovo.")

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
  alpha = input("Ângulo em graus: ")
  if alpha != "pi":
    sen = m.sin(m.radians(float(alpha)))
    print(round(sen, 4))
  else:
    print(0)

def cosseno():
  alpha = input("Ângulo em graus: ")
  if alpha != "pi":
    cos = m.cos(m.radians(float(alpha)))
    print(round(cos, 4))
  else:
    print(1)

def tangente():
  alpha = input("Ângulo em graus: ")
  if alpha != "pi":
    tg = m.tan(m.radians(float(alpha)))
    print(round(tg, 4))
  else:
    print(0)

def arc_seno():
  alpha = input("Qual é o valor do seno:")
  sen = m.degrees(m.asin(float(alpha)))
  print(f"Angulo em graus: {round(sen, 4)}")
  
def arc_cosseno():
  alpha = input("Qual é o valor do cosseno:")
  cos = m.degrees(m.acos(float(alpha)))
  print(f"Angulo em graus: {round(cos, 4)}")

def arc_tangente():
  alpha = input("Qual é o valor da tangente:")
  tg = m.degrees(m.atan(float(alpha)))
  print(f"Angulo em graus: {round(tg, 4)}")

#ALGEBRA

def formula_resolvente():
  a = input("Qual é o a?:")
  b = input("Qual é o b?:")
  c = input("Qual é o c?:")

  if (float(b) ** 2) - (4 * float(a) * float(c)) < 0:
    print("x pertene ao vazio!")
  else:
    x = (((0 - float(b)) + m.sqrt((float(b)**2) - (4 * float(a) * float(c))))/(2* float(a)))
    y = (((0 - float(b)) - m.sqrt((float(b)**2) - (4 * float(a) * float(c))))/(2* float(a)))
    print(f"x é igual a {x} ou {y}")

def casos_notaveis():
  print("Escolhe o caso notável:\n1.(x+y)^2\n2.(x+y)(x-y)")
  while True:
    escolha = input()
    if escolha == "1":
      x = input("Qual é o x?:")
      y = input("Qual é o y?:")
      c = ((float(x)**2) + (2 * float(x) * float(y)) + (float(y)**2))
      print(f"Resposta: {c}")
      break
    elif escolha == "2":
      x = input("Qual é o x?:")
      y = input("Qual é o y?:")
      c = (float(x)**2) - (float(y)**2)
      print(f"Resposta: {c}")
      break
    else:
      print("Não encontrei esse caso notável! Tenta denovo.")


#AREAS

def quadrado():
  l = input("Qual é o lado?:")
  area = float(l) ** 2
  print(f"A area do quadrado é {area}")

def retangulo():
  a = input("Qual é o primeiro lado?:")
  b = input("Qual é o segundo lado?:")
  area = float(a) * float(b)
  print(f"A área do retângulo é {area}")

def triangulo():
  b = input("Qual é a base?:")
  h = input("Qual é a altura?:")
  area = (float(b) * float(h)) / 2
  print(f"A área do triângulo é {area}")

def losango():
  DMaior = input("Qual é a diagonal maior?:")
  dmenor = input("Qual é a diagonal menor?:")
  area = (float(DMaior) * float(dmenor)) / 2
  print(f"A área do losango é {area}")

def trapezio():
  BaseMaior = input("Qual é a base maior?:")
  basemenor = input("Qual é a base menor?:")
  altura = input("Qual é altura?:")
  area = ((float(BaseMaior) + float(basemenor)) / 2) * float(altura)
  print(f"A área do trapézio é {area}")

def circulo():
  r = input("Qual é o raio?:")
  area = m.pi * (float(r) ** 2)
  print(f"A área do círculo é {area}")


#VOLUMES

def cubo():
  l = input("Qual é o lado?:")
  volume = float(l) ** 3
  print(f"O volume do cubo é {volume}")

def paralelepipedo():
  l1 = input("Qual é o primeiro lado?:")
  l2 = input("Qual é o segundo lado?:")
  l3 = input("Qual é o terceiro lado?:")
  volume = float(l1) * float(l2) * float(l3)
  print(f"O volume do paralelepípedo é {volume}")

def Prisma_regular():
  A = input("Qual é a área da base?:")
  h = input("Qual é a altura?:")
  volume =  float(A) * float(h)
  print(f"O volume do prisma é {volume}")

def cilindro():
  r = input("Qual é o raio da base?:")
  h = input("Qual é a altura?:")
  volume = m.pi * (float(r) ** 2) * float(h)
  print(f"O volume do cilindro é {volume}")

def cone():
  A = input("Qual é a área da base?:")
  h = input("Qual é a altura?:")
  volume = (float(A) / 3) * float(h)
  print(f"O volume do cone é {volume}")

def piramide():
  A = input("Qual é a área da base?:")
  h = input("Qual é a altura?:")
  volume = (float(A) / 3) * float(h)
  print(f"O volume da pirâmide é {volume}")

def esfera(): 
  r = input("Qual é o raio?:")
  volume = (4/3) * m.pi * (float(r) ** 3)
  print(f"O volume da esfera é {volume}")


#VETORES
def norma():
  v1 = input("Qual é o x do vetor?:")
  v2 = input("Qual é o y do vetor?:")
  norma = m.sqrt((float(v1) ** 2) + (float(v2) ** 2))
  print(f"A norma do vetor é {norma}")

def diferença_entre_pontos():
  Ax = input("Qual é o x do primeiro ponto)?:")
  Ay = input("Qual é o x do primeiro ponto)?:")
  Bx = input("Qual é o x do primeiro ponto)?:")
  By = input("Qual é o x do primeiro ponto)?:")
  X = float(Bx) - float(Ax)
  Y = float(By) - float(Ay)
  print(f"O vetor é ({X};{Y})")

def produto_escalar():
  u1 = input("Qual é o X do primeiro vetor?:")
  u2 = input("Qual é o Y do primeiro vetor?:")
  v1 = input("Qual é o X do segundo vetor?:")
  v2 = input("Qual é o Y do segundo vetor?:")
  produtoEscalar = (float(u1) * float(v1)) + (float(u2) * float(v2))
  print(f"O produto escalar dos vetores é {produtoEscalar}")

def angulo_vetor():
  u1 = input("Qual é o X do primeiro vetor?:")
  u2 = input("Qual é o Y do primeiro vetor?:")
  v1 = input("Qual é o X do segundo vetor?:")
  v2 = input("Qual é o Y do segundo vetor?:")
  produtoEscalar = (float(u1) * float(v1)) + (float(u2) * float(v2))
  normas = (m.sqrt((float(v1) ** 2) + (float(v2) ** 2))) * (m.sqrt((float(u1) ** 2) + (float(u2) ** 2)))
  cos = produtoEscalar / normas
  angulo = m.degrees(m.acos(cos))
  print(f"O angulo entre os dois vetores é {angulo} em graus")

#FISICA

#MOVIMENTO

def trabalho():
  f = input("Qual é a componente escalar da força?:")
  d = input("Qual é a distância?:")
  alpha = input("Qual é o angulo entre a força e o deslocamento?(em graus):")
  cos = m.cos(m.radians(float(alpha)))
  w = float(f) * float(d) * round(cos, 4)
  print(f"O trabalho da força é {w}")

def equacoes_movimento():
  print("Escolhe a equação:\n1. Equação do movimento\n2. Equação da velocidade")

  while True:
    equac = input()
    if equac == "1" or equac == "Equação do movimento":
      x0 = input("Qual é a posição inicial?(m):")
      v0 = input("Qual é a velocidade inicial?(m/s):")
      a = input("Qual é a aceleração?(m/s^2):")
      t = input("Qual é o tempo?(s):")

      x = float(x0) + float(v0) * float(t) + 0.5 * float(a) * (float(t) ** 2)

      print(f"A posição final é {x}")
      break
    elif equac == "2" or equac == "Equação da velocidade":
      v0 = input("Qual é a velocidade inicial?(m/s):")
      a = input("Qual é a aceleração?(m/s^2):")
      t = input("Qual é o tempo?(s):")

      v = float(v0) + float(a) * float(t)

      print(f"A velocidade final é {v}")
      break
    else:
      print("Não encontrei essa equação! Tenta denovo.")


#Movimento circular uniforme

def aceleracao_centripta():
  print("Qual formula preferes usar:\n1. a = V^2/R\n2. a = w^2 * r")
  while True:
    escola = input()
    if escola == "1" or escola == "a = V^2/R":
      v = input("Qual é a velocidade?:")
      r = input("Qual é o raio?:")
      a = (float(v) ** 2) / float(r)
      break
    elif escola == "2" or escola == "a = w^2 * r":
      w = input("Qual é a velocidade angular?:")
      r = input("Qual é o raio?:")
      a = (float(w) ** 2) * float(r)
      break
    else:
      print("Não encontrei essa opção! Tenta denovo.")
  print(f"A aceleração centrípta é {a}")


def velocidade_circulo():
  print("Escolhe qual valor usar:\n1. Velocidade angular\n2. Frequência\n3. Período")
  while True:
    escolha666 = input()
    if escolha666 == "1" or escolha666 == "Velocidade angular":
      w = input("Qual é a velocidade angular?:")
      r = input("Qual é o raio?:")
      v = float(w) * float(r)
      break
    elif escolha666 == "2" or escolha666 == "Frequencia":
      f = input("Qual é a frequência?:")
      r = input("Qual é o raio?:")
      v = 2 * m.pi * float(f) * float(r)
      break
    elif escolha666 == "3" or escolha666 == "Periodo":
      t = input("Qual é o período?:")
      r = input("Qual é o raio?:")
      v = ((2 * m.pi) / float(t)) * float(r)
      break
    else:
      print("Não encontrei essa opção! Tenta denovo.")
  print(f"A velocidade linear é {v}")


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
      print("Não encontrei essa opção! Tenta denovo.")
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
