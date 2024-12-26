import random
import time
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
  print("Powered by Cortex Corporation")
  time.sleep(0.5)
  print("Bem-vindo à TV-MLF :)")
