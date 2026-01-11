# Agora vamos solicitar uma string e um número intiero como entrada. Depois teremos que retornar
# a string repetida o número de vezes indicado pelo número inteiro com espaços entre elas.

texto = input("Digite uma string: ")
vezes = int(input("Digite um número inteiro: "))
resultado = (texto + " ") * vezes
print("String repetida:", resultado)
