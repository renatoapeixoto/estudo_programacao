'''Escape do Python e caracteres de novas linhas'''
print("A aranha pequenininha\nsubiu a tromba d'água.")
print()
print("abaixo veio a chuva\ne lavou a aranha.")
## A aranha pequenininha
## subiu a tromba d'água.
##
## abaixo veio a chuva
## e lavou a aranha.
## Curiosamente, enquantovocê pod

'''Usando vários argumentos'''
print("A aranha pequenininha" , "subiu" , "a tromba d'água.")
## A aranha pequenininha subiu a tromba d'água.
## Há uma chamada de função print(), mas ela contém três argumentos.
## Todos eles são cadeias de caracteres. Os argumentos são separados
## por vírgulas.

'''Concatenar'''
print("A aranha pequenininha" + "subiu" + "a tromba d'água.")

'''Argumentos de palavra-chave'''
print("Meu nome é", "Python.", end=" ")
print("Monty Python.")
## Meu nome é Python. Monty Python.
## Um argumento de palavra-chave consiste em três elementos:
## uma palavra-chave que identifica o argumento (end aqui);
## um sinal de igual (=); e um valor atribuído a esse argumento;
## Qualquer argumento de palavra-chave deve ser colocado após o último
## argumento posicional (isso é muito importante)
print("Meu", "nome", "é", "Monty", "Python.", sep="-")
print("Meu", "nome", "é", "Monty", "Python.", sep=" - ")
## Meu-nome-é-Monty-Python.
## Meu - nome - é - Monty - Python.
print("Meu", "nome", "é", sep="_", end=" *")
print("Monty", "Python.", sep="*", end="\n*")
## Meu_nome_é *Monty*Python.
## *
print("Programação","Essenciais","em", sep="***", end="...")
print("Python")
## Programação***Essenciais***em...Python
print("versão original:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("com menos 'print()' invocações:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("mais alto:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("dobrou:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)
