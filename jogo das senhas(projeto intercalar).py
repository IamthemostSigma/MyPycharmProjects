print("1 = fácil, 2 = médio, 3 = difícil")
nivel = input("Escolhe o nível: ")

if nivel == "1":
    a1 = input("Quanto é 9 ÷ 3? ")
    b2 = input("Qual é a cor da relva? ")
    c3 = input("Qual é o animal que mia? ")
    d4 = input("Qual é o contrário de dia? ")

    if a1 == "3".lower() and b2 == "verde".lower() and c3 == "gato".lower() and d4 == "noite".lower():
        print("6291")
    else:
        print("3217")

    senha1 = input("Qual é a senha? : ")
    if senha1 == "6291":
        print("Parabéns concluiste o modo fácil, a senha está correta!")
    else:
        print("A senha está errada, tente novamente!")

elif nivel == "2":
    a5 = input("Quanto é 12 x 6? ")
    b6 = input("Quanto é 15 x 3? ")
    c7 = input("Qual é a capital de Espanha? ")
    d8 = input("Qual é o maior planeta do sistema solar? ")
    e9 = input("Quantos minutos tem uma hora? ")

    if a5 == "72" and b6 == "45".lower() and c7 == "Madrid".lower() and (d8 == "júpiter".lower()) and e9 == "60".lower():
        print("28617")
    else:
        print("33153")

    senha2 = input("Qual é a senha? : ")
    if senha2 == "28617":
        print("Parabéns, concluiste o modo médio, a senha está correta!")
    else:
        print("A senha está errada, tente novamente!")

elif nivel == "3":
    a10 = input("Quanto é 9 x 7? ")
    b11 = input("Qual é o carro mais caro do mundo? ")
    c12 = input("Quanto é 144 ÷ 12? ")
    d13 = input("Qual é o carro mais rápido do mundo? ")
    e14 = input("Quem foi o primeiro pintor do mundo? ")
    f15 = input("Quem é o jogador mais rico do mundo? ")

    if a10 == "63" and b11 == "Rolls-Royce La Rose Noire Droptail".lower() and c12 == "12".lower() and d13 == "Koegnisegg Jesko Absolut".lower() and e14 == "Neandertais".lower() and f15 == "Faiq Bolkiah".lower():
        print("84392")
    else:
        print("11009")

    senha3 = input("Qual é a senha? : ")
    if senha3 == "84392":
        print("Parabéns, concluiste o modo difícil, a senha está correta!")
    else:
        print("A senha está errada, tente novamente!")
