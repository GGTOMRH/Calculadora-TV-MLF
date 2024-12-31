import calculos as c

def formulas():

    areas = ["Matemática", "Fisica", "Quimica"]

    materias = {
        "Matemática": ["Trignometria", "Geometria", ],
        "Fisica": ["Mecanica", "Energia", "Ondas e eletromagnetismo"],
        "Quimica": ["Quantidades", "Soluções"]
        }
    
    formulas = {
        "Trignometria": ["Seno", "Cosseno", "Tangente"],
        "Geometria": ["Teorema de Pitagoras"],
        "Mecanica": ...,
        "Energia": ... ,
        "Ondas e eletromagnetismo": ...,
        "Quantidades": ...,
        "Soluções": ...
                }

    print("Escolhe uma area: ")
    for i,area in enumerate(areas, start=1):
        print(f"{i}. {area}")

    while True:
        escolha = input()[0].capitalize()
        if escolha == "1" or escolha == "M":
            print("Escolhe uma matéria:")
            for i,materia in enumerate(materias["Matemática"], start=1):
                print(f"{i}. {materia}")
            while True:
                escolha2 = input()
                if escolha2 == "1" or escolha2 == materias["Matemática"][0]:
                    print("Escolhe uma formula:")
                    for i,formula in enumerate(formulas["Trignometria"], start=1):
                        print(f"{i}. {formula}")
                    while True:
                        escolha3 = input()
                        if escolha3 == "1" or escolha3 == "Seno":
                            c.seno()
                            break
                        elif escolha3 == "2" or escolha3 == "Cosseno":
                            c.cosseno()
                            break
                        elif escolha3 == "3" or escolha3 == "Tangente":
                            c.tangente()
                            break
                    break
                elif escolha2 == "2" or escolha2 == materias["Matemática"][1]:
                    print("gd")
                    break
                else:
                    print("Não encontrei essa matéria! Tenta denovo")
            break
        elif escolha == "2" or escolha == "F":
            print("Escolhe uma matéria:")
            for i,materia in enumerate(materias["Fisica"], start=1):
                print(f"{i}. {materia}")
            while True:
                escolha2 = input()
                if escolha2 == "1" or escolha2 == materias["Fisica"][0]:
                    print("mecanica")
                    break
                elif escolha2 == "2" or escolha2 == materias["Fisica"][1]:
                    print("emnergia")
                    break
                elif escolha2 == "3" or escolha2 == materias["Fisica"][1]:
                    print("ondas")
                    break
                else:
                    print("Não encontrei essa matéria! Tenta denovo")
            break
        elif escolha == "3" or escolha == "Q":
            print("Escolhe uma matéria:")
            for i,materia in enumerate(materias["Quimica"], start=1):
                print(f"{i}. {materia}")
            while True:
                escolha2 = input()
                if escolha2 == "1" or escolha2 == materias["Fisica"][0]:
                    print("quantidades")
                    break
                elif escolha2 == "2" or escolha2 == materias["Fisica"][1]:
                    print("solucoes")
                    break
                else:
                    print("Não encontrei essa matéria! Tenta denovo")
            break
        else:
            print("Não encontrei essa area! Tenta denovo!")

if __name__ == "__main__":
  formulas()
