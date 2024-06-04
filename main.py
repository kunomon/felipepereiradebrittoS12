class Principal:
    def _init_(self) -> None:
        pass

    while True:
        teste = input("Olá, sou o programa do Felipe, o que você deseja fazer?\n0. Deseja converter medidas?\n1. Deseja converter temperaturas?\n2. Encerrar programa?\n")
        if teste == "0":
            import conversor_medidas
        elif teste == "1":
            import conversor_temperatura
        elif teste == "2":
            print("Programa encerrado.")
            break
        else:
            print("Digite uma opção válida")
            input("Pressione Enter para continuar...")