class ConversorMedidas:
    def __init__(self) -> None:
        pass

converter1 = input("Se você deseja converter metros para centímetros, digite 1. Se você deseja converter centímetros para metros, digite 2:\n")

if converter1 == "1":
    conversor1 = float(input("Digite os metros que deseja converter para centímetros:\n")) * 100
    print(f"O valor convertido é {conversor1} centímetros.")
elif converter1 == "2":
    conversor2 = float(input("Digite os centímetros que deseja converter para metros:\n")) / 100
    print(f"O valor convertido é {conversor2} metros.")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
