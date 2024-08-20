# 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada: 
# a) de 1 até 10, de 1 em 1      
# b) de 10 até 0, de 2 em 2                  
# c) uma contagem personaliza
def texto(msg):
    tamanho = len(msg) + 4
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)



def contador(i, f, p):
    print(f'Contagem de {1}, até {f} de {p} em {p}')

    if i < f:
        contador = i
        while contador <= f:
            print(f'{contador} ', end=' ')
            contador += p
        print('Fim!')
    else:
        contador = i
        while contador >= f:
            print(f'{contador} ', end='')
            contador -= p
        print('Fim')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)