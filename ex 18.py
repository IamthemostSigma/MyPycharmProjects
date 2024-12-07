vcdut = int(input("A que velocidade passaste do radar?"))

limite = "80"

if vcdut >=80:
    calculo = (vcdut - 80) * 2
    print(f"Passaste o limite tens de pagar uma multa de {calculo} euros")
else:
    print("Não ultrapassas-te o limite. Boa viagem")