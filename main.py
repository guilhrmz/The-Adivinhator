import time

print("------------------------------")
print("The Advinhator")
print("------------------------------")

Pensar = input("Escolha um Numero:")

def Advinhator():
    time.sleep(2)
    print("CALCULANDO PROBABILIDADES....")
    time.sleep(2)
    print("ENTRANDO NA SUA MENTE....")
    time.sleep(2)
    print("ANALISANDO O CORTEX PRÉ FRONTAL....")
    time.sleep(2)
    print("DESCRIPTOGRAFANDO....")
    time.sleep(3)
    print("ANALISANDO....")
    time.sleep(4)
    print("EUREKA!!!")
    time.sleep(1)
    print("SEU NUMERO É......")
    time.sleep(2)
    print(Pensar)
    time.sleep(2)
    Correto = int(input("Seu numero está Correto?\n1-Sim\n2-Não"))
    if Correto == 1:
        print("--------------------------------")
        print("           Vitoria              ")
        print("--------------------------------")
    else:
        print("--------------------------------")
        print("         MENTIROSO!!!!          ")
        print("--------------------------------")

Advinhator()