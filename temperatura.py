class Temperatura:
    def __init__(self) -> None:
        pass


while True:
    converter = input("Se você deseja converter de Fahrenheit para Celsius, digite 1. Se você deseja converter de Celsius para Fahrenheit, digite 2:\n")
    if converter in ["1", "2"]:
        break
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if converter == "1":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit:\n"))
    celsius = (fahrenheit - 32) * 5/9
    print(f"A temperatura convertida é {celsius:.2f} graus Celsius.")
elif converter == "2":
    celsius = float(input("Digite a temperatura em Celsius:\n"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura convertida é {fahrenheit:.2f} graus Fahrenheit.")

while True:
    teste2 = input("Programa encerrado. Deseja voltar para a tela inicial? Se sim, digite 1. Se quiser encerrar o programa, digite 0: ")
    if teste2 in ["0", "1"]:
        break
    else:
        print("Selecione uma opção válida")

if teste2 == "0":
    print("Programa encerrado.")
elif teste2 == "1":
    input("Pressione Enter para continuar...")
import main
