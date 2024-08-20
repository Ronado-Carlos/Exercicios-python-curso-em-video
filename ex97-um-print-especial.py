# Ex 97 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamnho adaptável.
def texto(msg):
    tamanho = len(msg) + 4
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)


texto('Ronaldo Carlos Corrêa')
texto('Aprenda Python')
texto('Python')