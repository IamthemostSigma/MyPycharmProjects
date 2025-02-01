pesos = ["10kg", "20kg", "30kg", "40kg", "50kg"]
for x in range(1):
    pergunta = int(input("Escolhe um número da tabuada de 10 até 50(escreva sem kg)!"))
    if pergunta >=50:
        print("50kg é o maior peso")
    if pergunta <=10:
        print("10kg é o menor peso")
    if pergunta >20<40>50:
        print(f"{pergunta}kg é o peso médio")