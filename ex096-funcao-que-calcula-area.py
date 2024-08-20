# Ex 96 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é de {a}m².')


def cabecalho(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

cabecalho('CONTROLE DE TERRENOS')
larg = float(input('Qual a largura em m²:? '))
comp = float(input('Qual o comprimento em m²:? '))
area(larg, comp)