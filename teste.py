def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")

def calculadora():
    while True:
        # Solicita ao usuário para inserir dois números
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        # Solicita ao usuário para escolher uma operação
        print("\nEscolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        operacao = input("Digite o número da operação desejada: ")

        # Realiza a operação escolhida
        if operacao == '1':
            resultado = num1 + num2
            print(f"A soma de {num1} e {num2} é: {resultado}")
        elif operacao == '2':
            resultado = num1 - num2
            print(f"A subtração de {num1} por {num2} é: {resultado}")
        elif operacao == '3':
            resultado = num1 * num2
            print(f"A multiplicação de {num1} por {num2} é: {resultado}")
        elif operacao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"A divisão de {num1} por {num2} é: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Operação inválida. Por favor, escolha uma operação válida.")

        # Pergunta se o usuário deseja realizar outra operação
        novamente = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if novamente != 's':
            break

if __name__ == "__main__":
    calculadora()
