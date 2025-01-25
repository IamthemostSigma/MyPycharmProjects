numero_inicial=int(input("Escolha o número inicil: "))
numero_final=int(input("Escolha o número final: "))
par_impar=int(input("Quer números pares[1] ou impares[2]?: "))

soma=0

if par_impar==1:
    print("Os números pares são: ")

if par_impar ==2:
    print("Os números impares são: ")

#verificação de números pares ou impares

for x in range(numero_inicial, numero_final+1):
    if par_impar ==1:
        if x%2==0:
            print(x, end= " ")
        elif par_impar==2:
            if x%2==1:
                print(x, end= " ")
                soma+=1
        else:
            print("Opção inválida!")
            break

if par_impar==1:
    print()