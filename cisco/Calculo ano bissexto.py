# Calculo ano bissexto
'''
ano = int(input("Digite um ano: "))

if ano > 1581 :
     if ano % 4 == 0 :
         if (ano % 100)  == 0 :
             if (ano % 400) == 0  :    
                 print("Ano bissexto")
             else :
                 print("Ano comum")
         else:
             print("Ano bissexto")   
     else :
          print("Ano comum")
else :
    print("Não está dentro do período do calendário gregoriano")
'''
##########################################################

ano2 = int(input("Digite um ano: "))

if ano2 < 1582:
 print("Não dentro do período do calendário gregoriano")
else:
   if ano2 % 4 != 0:
     print("ano comum")
   elif ano2 % 100 != 0:
     print("Ano bissexto")
   elif ano2 % 400 != 0:
     print("ano comum")
   else:
     print("Ano bissexto")
