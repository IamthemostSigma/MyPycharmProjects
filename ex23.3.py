# Pede o numero inicial
numero_inicial = int(input("Digite o número inicial"))

# Pede o numeor final
numero_final = int(input("Digite o número final"))

# Pede ao jodador o incremento(passos)
incremento = int(input("Digite o incremento(passos): "))

# Exibe todos os números entre o numero inical e o final com o incremento especificado
print(f"Os números entre {numero_inicial} e {numero_final} com incremento de {incremento} são: ")
for i in range(numero_inicial, numero_final + 1, incremento):
    print(i)