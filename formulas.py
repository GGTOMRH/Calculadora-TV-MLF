def formulas():
    areas = ["Matemática", "Fisica", "Quimica"]
    formulas = {
        "Matemática": ["Trignometria", "Geometria", ],
        "Fisica": ["Mecanica", "Energia", "Ondas e eletromagnetismo"],
        "Quimica": ["Quantidades", "Soluções"]
        }
    print("Escolhe uma area: ")
    for i,area in enumerate(areas, start=1):
        print(f"{i}. {area}")

    while True:
        escolha = input()[0].capitalize() 
        if escolha == "1" or escolha == "M":
            print("Escolhe uma matéria:")
            for i,materia in enumerate(formulas["Matemática"], start=1):
                print(f"{i}. {materia}")
            while True:
                escolha2 = input()
                if escolha2 == "1" or escolha2 == formulas["Matemática"][0]:
                    print("trig")
                    break
                elif escolha2 == "2" or escolha2 == formulas["Matemática"][1]:
                    print("gd")
                    break
                else:
                    print("Não encontrei essa matéria! Tenta denovo")
            break
        elif escolha == "2" or escolha == "F":
            print("Escolhe uma matéria:")
            for i,materia in enumerate(formulas["Fisica"], start=1):
                print(f"{i}. {materia}")
            while True:
                escolha2 = input()
                if escolha2 == "1" or escolha2 == formulas["Fisica"][0]:
                    print("mecanica")
                    break
                elif escolha2 == "2" or escolha2 == formulas["Fisica"][1]:
                    print("emnergia")
                    break
                elif escolha2 == "3" or escolha2 == formulas["Fisica"][1]:
                    print("ondas")
                    break
                else:
                    print("Não encontrei essa matéria! Tenta denovo")
            break
        elif escolha == "3" or escolha == "Q":
            print("Escolhe uma matéria:")
            for i,materia in enumerate(formulas["Quimica"], start=1):
                print(f"{i}. {materia}")
            while True:
                escolha2 = input()
                if escolha2 == "1" or escolha2 == formulas["Fisica"][0]:
                    print("quantidades")
                    break
                elif escolha2 == "2" or escolha2 == formulas["Fisica"][1]:
                    print("solucoes")
                    break
                else:
                    print("Não encontrei essa matéria! Tenta denovo")
            break
        else:
            print("Não encontrei essa area! Tenta denovo!")
