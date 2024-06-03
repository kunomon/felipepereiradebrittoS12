class Principal:
    def __init__(self) -> None:
        pass
while True:
    teste = input("Olá, sou o programa do Felipe.\nVocê deseja converter temperaturas? \n0. Não\n1. Sim \n")
    if teste in ["0", "1"]:
        break
    else:
        print("Digite uma opção válida")

input("Pressione Enter para continuar...")

if teste == "1":
    from temperatura import Temperatura
elif teste == "0":
    while True:
        oi = input("Você não optou por converter temperaturas. Deseja converter medidas? \n1. Sim \n2. Encerrar programa:\n").capitalize()
        if oi in ["1", "2"]:
    
            break
        else:
            print("Digite uma opção válida")
    if oi == "1":
        from cmparam import ConversorMedidas
    elif oi == "2":
        print("Programa encerrado")