class Principal:
    def __init__(self) -> None:
        pass
while True:
    teste = input("Olá, sou o programa do Felipe. Você deseja converter temperaturas? Se sim, digite 1. Se não, digite 0: ")
    if teste in ["0", "1"]:
        break
    else:
        print("Digite uma opção válida")

input("Pressione Enter para continuar...")

if teste == "1":
    from temperatura import Temperatura
elif teste == "0":
    while True:
        oi = input("Você não optou por converter temperaturas. Deseja converter medidas? Se sim, digite 'Medidas' se quer encerrar o programa digite 'Encerrar': ").capitalize()
        if oi in ["Medidas", "Encerrar"]:
    
            break
        else:
            print("Digite uma opção válida")
    if oi == "Medidas":
        from cmparam import ConversorMedidas
    elif oi == "Encerrar":
        print("Programa encerrado")