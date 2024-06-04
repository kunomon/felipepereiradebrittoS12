class Principal:
    def _init_(self) -> None:
        pass

    while True:
        teste = input("Olá, sou o programa do Felipe, o que você deseja fazer?\n1. Deseja converter medidas?\n2. Deseja converter temperaturas?\n3. Encerrar programa?\n")
        if teste == "1":
            import conversor_medidas
        elif teste == "2":
            import conversor_temperatura
        elif teste == "3":
            print("Programa encerrado.")
            break
        else:
            print("Digite uma opção válida")
            input("Pressione Enter para continuar...")