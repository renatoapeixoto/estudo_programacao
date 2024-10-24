#############################################

#loop infinito
while True:
    print("Estou preso dentro de um loop.")

##############################################

# Loop existe uma condição para terminar o loop  
# Armazene o maior número atual aqui.
largest_number = -999999999
 
# Insira o primeiro valor.
number = int(input("Digite um número ou digite -1 para parar: "))
 
# Se o número não for igual a -1, continue.
while number != -1:  # Se digitar o -i o loop termina
    # O número é maior que o maior_número?
    if number > largest_number:
        # Sim, atualize o maior_número.
        largest_number = number
    # Insira o próximo número.
    number = int(input("Digite um número ou digite -1 para parar: "))
 
# Imprima o maior número.
print("O maior número é:", largest_number)

#############################################

# Um programa que lê uma sequência de números
# e conta quantos números são pares e quantos são ímpares.
# O programa termina quando zero é digitado.
 
odd_numbers = 0
even_numbers = 0
 
# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))
 
# 0 termina a execução.
while number != 0:
    # Verifique se o número é ímpar.
    if number % 2 == 1:
        # Aumente o contador odd_numbers.
        odd_numbers += 1
    else:
        # Aumente o contador even_numbers.
        even_numbers += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))
 
# Imprimir resultados.
print("Números ímpares contam:", odd_numbers)
print("Números pares contam:", even_numbers)

#############################################

# Loop usa uma variavel de contador 
counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)

#############################################

for i in range(4): # 0,1,2,3
   print("O valor de i é atualmente", i)

for i in range(2, 8):  # 2,3,4,5,6,7
    print("O valor de i é atualmente", i)

for i in range(2, 10, 2): # 2,4,6,8 o terceiro elemento é incremento
  print("O valor de i é atualmente", i)

#############################################

# break - exemplo
print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")
##O break instrução:
##Dentro do laço. 1
##Dentro do laço. 2
##Fora do loop.

# continue - exemplo
print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")
##O continue instrução:
##Dentro do laço. 1
##Dentro do laço. 2
##Dentro do laço. 4
##Dentro do laço. 5
##Fora do loop.

#############################################

maior_numero = - 9999999999
contador = 0

while True:
    numero = float(input("Digite um número ou digite -1 para terminar o programa: "))
    if numero == -1 :
        break
    contador += 1
    if numero > maior_numero:
        maior_numero = numero

if contador != 0:
    print("TO maior número é", maior_numero)
else:
    print("Você não inseriu nenhum número.")

#############################################

largest_number = - 99999999
counter = 0

number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

if counter:
    print("O maior número é",  largest_number)
else:
    print("Você não inseriu qualquer número.")

#############################################

## while com else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
## else:: A parte else do laço só executa quando o laço termina normalmente,
## ou seja, quando a condição do while (nesse caso, i < 5) deixa de ser verdadeira.















