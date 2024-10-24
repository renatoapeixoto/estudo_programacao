
##   OPERADORES EM PYTHON

##  tabela de prioridade
##  1 - **
##  2 - * , / , // , %
##  3 - < , <= , > , > =
##  4 - == , != 



''' Adição '''
print(-4 + 4)         #  0
print(-4.0 + 8)      #  4.0

''' Subtracao '''
print(-4 - 4)          #  - 8
print(4. - 8)          #  - 4.0       Obs:  4.  -  O ponto representa valor float , seria igual a 4.0
print(-1.1)            #  - 1.1

''' Exponenciação '''
print(2 ** 3)         #  8
print(2 ** 3.)        #  8.0
print(2. ** 3)        #  8.0
print(2. ** 3.0)     #  8.0
print (2 ** 2 ** 3 )        # 256    OBS: O  operador de exponenciação usa a associação do lado direito para o esquerdo.
print ((2 ** 2) ** 3 )      # 64


##'  Lembre-se : É possível formular as seguintes regras com base neste resultado:
##  Quando os dois ** argumentos são inteiros, o resultado também é um número inteiro;
##  Quando pelo menos um argumento ** é um float, o resultado também é um float. '''

'''  Multiplicação   '''
print(2 * 3)          #  6
print(2 * 3.)         #  6.0
print(2. * 3)         #  6.0
print(2. * 3.0)      #  6.0

''' Divisão  -  O resultado produzido pelo operador de divisão é sempre um float'''
print(6 / 3)        #  2.0
print(6 / 3.)       #  2.0
print(7 / 3)        #  2.3333333333333335
print(7. / 3.)      #  2.3333333333333335
resultado = 7 / 3    # Vamos formatar a saida de dados
print(f"O resultado é : {resultado: .2f}")  # Saída: 2.33

'''  Divisão de número inteiro tem que usar  barra barra   //   '''
print(6 // 3)           #  2            # Só da inteiro se os dois numeros for inteiro.
print(6 // 3.)          #  2.0          
print(15 // 4)         # 3             OBS: O resultado é 3,75 porém sempre arrendoda para o menor valor do inteiro
print(6 // 4)           # 1             OBS: O resultado é 1,5 porém sempre arrendoda para o menor valor do inteiro
print(-15. // 4)        # -4.0       OBS: O resultado é 3,75 porém sempre arrendoda para o menor valor do inteiro
print(-6 // 4 )         # -2           OBS: O resultado é 1,5 porém sempre arrendoda para o menor valor do inteiro

''' Calcular o resto da divisão  %  '''
print( 10 % 10  )  #  resposta: 0  ->  orden  %  *   +

''' Prioridades  '''
##  Parênteses ( ())
##  Exponenciação ( **)
##  Multiplicação ( *), Divisão ( /), Módulo ( %), Divisão inteira ( //) — da esquerda para a direita
##  Adição ( +), Subtração ( -) — da esquerda para a direita 

print(10 + 10 - 10 ** 3 * 5 % 3  / 10 )     # 19,8
##  Resumir os Passos:
##  10 ** 3→1000
##  1000 * 5→5000
##  5000 % 3→2
##  2 / 10→0.2
##  10 + 10 - 0.2→19.8
##  Portanto, o resultado da expressão é 19,8

print(10 + 10 - 10 ** 3 * 5 % 3 // 10)  # Saída: 20
##  Resumir os Passos:
##  10 ** 3→1000
##  1000 * 5→5000
##  5000 % 3→2
##  2 // 10→0
##  10 + 10 - 0→20
##  Portanto, o resultado da expressão é 20 .

print((10 + 10 - 10 ** 3 * 5 % 3 / 10) // 1)  # Saída: 19.0
##  Resumir
##  10 ** 3→1000
##  1000 * 5→5000
##  5000 % 3→2
##  2 / 10→0.2
##  10 + 10 - 0.2→ 19.8
##  19.8 // 1→ 19.0
##  Portanto, o resultado da expressão é 19.0 

print((2 ** 4), (2 * 4.), (2 * 4))     #  16   8.0    8
 
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))       #  -0.5    0.5    0    -1
 
print((2 % -4), (2 % 4), (2 ** 3 ** 2))     #   -2     2     512
 

'''  OPERADORES DE COMPARAÇÃO  '''
'''  Igualdade  ==   '''
print(2==2)         # True
print(2==2.)        # True
print(2==2.0)      # True
print(2==1)         # False

'''  Difrente ou desigualdade  !=   '''
var = 0  
print(var != 0)    # False
var = 1  
print(var != 0)   # True

'''  Maior ou igual a  >=   '''
a = 2
b = 3
c = 2
print ( a >= b )   #  False
print ( a >= c )   #  True

'''  Menor ou igual a  <=   '''
print ( a <= b )   # True
print ( a <= c )   # True








