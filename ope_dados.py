# Vamos ter como entrada dois números e depois realizar uma operação simples entre eles, como soma,
# subtração, multiplicação ou divisão.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")
