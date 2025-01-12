import calculos as c

def formulas():

    areas = ["Matemática", "Fisica", "Quimica"]

    materias = {
        "Matemática": ["Trignometria", "Geometria", "Algebra", "Áreas", "Volumes", "Vetores"],
        "Fisica": ["Mecanica", "Energia", "Ondas e eletromagnetismo"],
        "Quimica": ["Quantidades", "Soluções"]
        }
    
    formulas = {
        "Trignometria": ["Rad -> Grau / Grau -> Rad ", "Seno", "Cosseno", "Tangente", "ArcSeno", "ArcCosseno", "ArcTangente" , "Formulas Fundamentais"],
        "Geometria": ["Teorema de Pitagoras", "Teorema de pitagoras inverso", "Distancia entre dois pontos"],
        "Algebra": ["Formula Resolvente", "Casos notáveis"],
        "Areas": ["Quadrado", "Retângulo", "Triangulo", "Losango", "Trapezio", "Circulo"],
        "Volumes": ["Cubo", "Paralelepípedo", "Prisma Regular","Pirâmide", "Cilindro", "Cone", "Esfera"],
        "Vetores": ["Diferença de dois pontos", "Norma", "Produto Escalar", "Angulo entre dois vetores"],

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
                        if escolha3 == "1" or escolha3 == "Rad -> Grau / Grau -> Rad ":
                            c.radian_degrees()
                            break
                        elif escolha3 == "2" or escolha3 == "Seno":
                            c.seno()
                            break
                        elif escolha3 == "3" or escolha3 == "Cosseno":
                            c.cosseno()
                            break
                        elif escolha3 == "4" or escolha3 == "Tangente":
                            c.tangente()
                            break
                        elif escolha3 == "5" or escolha3 == "ArcSeno":
                            c.arc_seno()
                            break
                        elif escolha3 == "6" or escolha3 == "ArcCosseno":
                            c.arc_cosseno()
                            break
                        elif escolha3 == "7" or escolha3 == "ArcTangente":
                            c.arc_tangente()
                            break
                        elif escolha3 == "8" or escolha3 == "Formulas Fundamentais":
                            c.formulas_fundamentais()
                            break
                        else:
                            print("Não encontrei essa formulas! Tenta denovo.")
                    break
                elif escolha2 == "2" or escolha2 == materias["Matemática"][1]:
                    print("Escolhe uma formula:")
                    for i,formula in enumerate(formulas["Geometria"], start=1):
                        print(f"{i}. {formula}")
                    while True:
                        escolha3 = input()
                        if escolha3 == "1" or escolha3 == "Teorema de pitagoras":
                            c.teorema_de_pitagoras()
                            break
                        elif escolha3 == "2" or escolha3 == "Teorema de pitagoras oposto":
                            c.teorema_de_pitagoras_oposto()
                            break
                        elif escolha3 == "3" or escolha3 == "Distancia entre 2 pontos":
                            c.distancia()
                            break
                        else:
                            print("Não encontrei essa formulas! Tenta denovo.")
                    break
                elif escolha2 == "3" or escolha2 == materias["Matemática"][2]:
                    print("Escolhe uma formula:")
                    for i,formula in enumerate(formulas["Algebra"], start=1):
                        print(f"{i}. {formula}")
                    while True:
                        escolha3 = input()
                        if escolha3 == "1" or escolha3 == "Formula resolvente":
                            c.formula_resolvente()
                            break
                        elif escolha3 == "2" or escolha3 == "Casos notáveis":
                            c.casos_notaveis()
                            break
                        else:
                            print("Não encontrei essa formulas! Tenta denovo.")
                    break
                elif escolha2 == "4" or escolha2 == materias["Matemática"][3]:
                    print("Escolhe uma formula:")
                    for i,formula in enumerate(formulas["Areas"], start=1):
                        print(f"{i}. {formula}")
                    while True:
                        escolha3 = input()
                        if escolha3 == "1" or escolha3 == "Quadrado":
                            c.quadrado()
                            break
                        elif escolha3 == "2" or escolha3 == "Retangulo":
                            c.retangulo()
                            break
                        elif escolha3 == "3" or escolha3 == "Triangulo":
                            c.triangulo()
                            break
                        elif escolha3 == "4" or escolha3 == "Losango":
                            c.losango()
                            break
                        elif escolha3 == "5" or escolha3 == "Trapezio":
                            c.trapezio()
                            break
                        elif escolha3 == "6" or escolha3 == "Circulo":
                            c.circulo()
                            break
                        else:
                            print("Não encontrei essa formulas! Tenta denovo.")
                    break
                elif escolha2 == "5" or escolha2 == materias["Matemática"][4]:
                    print("Escolhe uma formula:")
                    for i,formula in enumerate(formulas["Volumes"], start=1):
                        print(f"{i}. {formula}")
                    while True:
                        escolha3 = input()
                        if escolha3 == "1" or escolha3 == "Cubo":
                            c.cubo()
                            break
                        elif escolha3 == "2" or escolha3 == "Paralelepipedo":
                            c.paralelepipedo()
                            break
                        elif escolha3 == "3" or escolha3 == "Prisma Regular":
                            c.Prisma_regular()
                            break
                        elif escolha3 == "4" or escolha3 == "Piramide":
                            c.piramide()
                            break
                        elif escolha3 == "5" or escolha3 == "Cilindro":
                            c.cilindro()
                            break
                        elif escolha3 == "6" or escolha3 == "Cone":
                            c.cone()
                            break
                        elif escolha3 == "7" or escolha3 == "Esfera":
                            c.esfera()
                            break
                        else:
                            print("Não encontrei essa formulas! Tenta denovo.")
                    break
                elif escolha2 == "6" or escolha2 == materias["Matemática"][5]:
                    print("Escolhe uma formula:")
                    for i,formula in enumerate(formulas["Vetores"], start=1):
                        print(f"{i}. {formula}")
                    while True:
                        escolha3 = input()
                        if escolha3 == "1" or escolha3 == "Diferença de dois pontos":
                            c.diferença_entre_pontos()
                            break
                        elif escolha3 == "2" or escolha3 == "Norma":
                            c.norma()
                            break
                        elif escolha3 == "3" or escolha3 == "Produto escalar":
                            c.produto_escalar()
                            break
                        elif escolha3 == "4" or escolha3 == "Angulo entre dois vetores":
                            c.angulo_vetor()
                            break
                        else:
                            print("Não encontrei essa formulas! Tenta denovo.")
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
