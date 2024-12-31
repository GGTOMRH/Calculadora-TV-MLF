from formulas import formulas

#função do menu de ajudas
def calc_help():
  helps: list[str] = ["Simbolos", "Formulas", "Calculadora", "Outro"]
  print("Escolhe o tipo de ajuda: ")
  for i, ajuda in enumerate(helps, start=1):  #mostra as ajudas possiveis
    print(f"{i}. {ajuda}")
  while True:
    ajuda: str = input().capitalize()
    if ajuda == "Simbolos" or ajuda == "1": #Ajuda dos simbolos
      print("\nTodos os simbolos:\n")
      print("O + representa adição")
      print("O * representa multiplicação")
      print("O - representa subtração")
      print("A / representa divisão")
      print("O ^ coloca o numero em expoente")
      print("A # representa raiz quadrada")
      break
    elif ajuda == "Formulas" or ajuda == "2": #ajuda das formulas(ver formulas.py)
      formulas()
      break
    elif ajuda == "Calculadora" or ajuda == "3":  #ajuda da calculadora apenas fala um pouco da calculadora
      print("A calculadora TV-MLF é o primeiro modelo da cortex corporation.")
      print("Ela funciona de uma forma muito simples, ao colocar as contas no terminal,")
      print("Ela executa o nosso programa secreto\n")
      print("Para além disso ela vem com formulas especiais no seu codigo")
      print("Espero que goste do nosso produto!")
      break
    elif ajuda == "Outro" or ajuda == "4":  #ajuda outro mostra o email da empresa
      print("\nNão sabemos como ajudá-lo! \nQualquer questão entre em contacto através do nosso email:\ncortexcorporationpt@gmail.com\n")
      break
    else:
      print("Não encontrei a tua ajuda, tenta denovo!")
