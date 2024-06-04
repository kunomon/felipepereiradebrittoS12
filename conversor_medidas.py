class ConversorMedidas:
    def __init__(self) -> None:
        pass

while True:
    converter1 = input("Qual opção você deseja?\n1. Converter metros para centímetros\n2. Converter centímetros para metros\n")
    if converter1 in ["1", "2"]:
        break
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

while True:
    oi2 = input("Pressione Enter para continuar...")
    if oi2 == "":
        break
    else:
        print("Por favor, pressione apenas 'Enter'.")

if converter1 == "1":
    conversor1 = float(input("Digite os metros que deseja converter para centímetros:\n")) * 100
    print(f"O valor convertido é {conversor1} centímetros.")
elif converter1 == "2":
    conversor2 = float(input("Digite os centímetros que deseja converter para metros:\n")) / 100
    print(f"O valor convertido é {conversor2} metros.")

while True:
    teste2 = input("Deseja voltar para a tela inicial?\n1. Voltar para tela inicial \n2. Encerrar programa\n")
    if teste2 in ["2", "1"]:
        break
    else:
        print("Selecione uma opção válida.")
if teste2 == "2":
    print("Programa encerrado.")
    exit()
elif teste2 == "1":
    import limpartexto
    import main