# faca um algoritimo que leia tres valores inteiros, e imprima o menor deles.
# Algoritmo para ler três valores inteiros e imprimir o menor deles

# Variaveis
menor: int

# Leitura dos valores inteiros direto na variavel
valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

# verificar o menor valor
if valor1 < valor2 and valor1 < valor3:
    menor = valor1
elif valor2 < valor3:
    menor = valor2
else:
    menor = valor3
# menor = min(valor1, valor2, valor3)  # funcao min - > menor

# Impressão do menor valor
print("O menor valor", "dos numeros", sep=" - ", end=" ")
print(f"digitado\né: {menor}")

# O menor valor - dos numeros digitado
# é:

# Sep=" - " -> coloca um separador no texto
# end=" " -> Continua o texto da linha abaixo
# \n -> pula para a linha abaixo
