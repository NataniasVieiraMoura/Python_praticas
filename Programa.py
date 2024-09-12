
#pp1
'''Comentários em python são com 3 aspas(apenas em linhas sem código) e
 # (cerquilha) em qualquer parte do texto'''
#Remova as cerquilhas para ver funcionando
#Separei os códigos por espaços. Cuidado ao remover de todos.
#Ums códigos podem atrapalhar os outros;
#Para executar no terminal utilize: Ctrol + Shift + f10
#Para executar novamente o mesmo código no terminal digite: Ctrol + f5

#coah = input('Digite um valor:')
#print(type(coah))
'''O método type indica a que classe o tipo primitivo da váriavel é.'''
'''Funções int(inteiro),float(número real),bool(verdadeiro ou falso)
str(nomes,string,caracter, ''(string vazia))'''

'''Imput: pede um valor no terminal para uma variável receber'''
'''Print: exibe no terminal'''
'''Função is'''
'''Métodos is retornam True ou False sobre a variável:
isnumeric() : é número?
isalpha() : é letra?
isalnum() : é letra ou número?
isupper() : está em maiúsculo?
islower() : está em minusculo?
isdecimal():  é um número decimal?
isspace() : o texto é o espaço do teclado?
'''
#cs = input('Digite algo:')
#print('É um número?',cs.isnumeric())
#print('É uma letra?',cs.isalpha())
#print('É um alfanumerico?',cs.isalnum())
#print('É um nome minúsculo?',cs.islower())
#print('É um nome maiúsculo?',cs.isupper())
#print('É um decimal?',cs.isdecimal())
#print('É o spaço do teclado?',cs.isspace())

'''Operadores aritimeticos:
 - subtração
 + adição
 * multiplicação
 / divisão
 //divisão inteira
 % resto da divisão'''

'''Ordem de precedencia:
 1º parentesis ()
 2º potêmcia **
 3º divisão, multiplicação, divisão inteira, resto da divisão /, //, *, % (o que aparecer primeiro)
 4º soma, subtração -, + (o que aparecer primeiro)'''

#print('oi'+'olá')
#print('oi'* 10)
#print('$'*20)
#coa = input(str('Hello, what is your name:'))
'''O format serve para inserir no texto variáveis e etc...
    Para que o elemento do format apareça no texto digite {} dentro do texto no local desejado'''
#print('Nice to meet you {:20}!'.format(coa))
'''Dentro das chaves que estão dentro do texto: você pode acrecentar espaços
junto do elemento escolhido. No caso da linha 57 adiciona-se 20 espaços junto
ao texto'''
#print('Nice to meet you {:>20}!'.format(coa))
'''Na linha acima faz a mesma coisa, mas o simbolo de maior/menor especifica
se você que adicionar á esquerda ou a direita'''
#print('Nice to meet you {:<20}!'.format(coa))
#print('Nice to meet you {:^20}!'.format(coa))
'''Na linha acima adiciona espaços de ambos os lados do elemento inserido'''
#print('Nice to meet you {:$^15}!'.format(coa))
'''Acima: você pode especificar o elemento que deseja aparecer, no caso, de ambos os lados'''

#a = 1
#b = 2
#c = 3
#s = a + b + c
#d = c / b
#m = a * b * c
#di = c // b
#e = c **b
#print('Seja a: {},b {} e c {}'.format(a, b, c))
#print('Soma de a,b e c: {},Divisão de c por b: {} '.format(s, d))
#print('Multiplicação de a, b e c: {} ,Divisão inteira de c por b: {}'.format(m, di))
#print('Potência de c elevado a e b: {} '.format(e))


#print('Para a produção de peças de chadres\n é necessário a criação de ferramentas produtivas.',end='')
#print('Dentre elas se destaca lixas giratorias\n e um suporte que fixe a peça que rotacionará.')
'''O \n coloca o resto do texto em outra linha'''
'''O ,end='' une a linha posterior com a anterior'''

'''Peguei todas as funções das aulas 1 até a 7'''

