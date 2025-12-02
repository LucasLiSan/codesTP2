def calculadora():
    while True:
        print("\n=== Calculadora Simples ===")
        print("Operações disponíveis:")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Sair")

        escolha = input("Escolha a operação (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora...")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Digite apenas números válidos!")
            continue

        if escolha == '1':
            resultado = num1 + num2
            op = '+'
        elif escolha == '2':
            resultado = num1 - num2
            op = '-'
        elif escolha == '3':
            resultado = num1 * num2
            op = '*'
        elif escolha == '4':
            if num2 == 0:
                print("Erro: Divisão por zero!")
                continue
            resultado = num1 / num2
            op = '/'

        print(f"{num1} {op} {num2} = {resultado}")

# Executa a calculadora
calculadora()
