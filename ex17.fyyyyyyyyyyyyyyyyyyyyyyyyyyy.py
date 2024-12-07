R = "Residencias"
I = "Industrias"
C = "Comercios"
tipo = input("Qual é a tua instalação de kWh? Residencias(R) Industrias(I) Comercios(C)")
quantidade = int(input("Qual é a quantidade de kWh que consomes?"))

if quantidade <=500 and R:
    print("Tens de pagar 0,40")
elif quantidade >500 and R:
    print("Tens de pagar 0,55")