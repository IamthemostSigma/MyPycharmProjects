# solicitando ao usuario um número
numero = int(input("Digite um número:  "))

# Exibindo todos os números que antecedem o número fornecido
print(f"Os números que antecedem {numero} são:")
for i in range(numero):
    print(i)