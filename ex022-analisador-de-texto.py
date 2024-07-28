# 22-Crie um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas,
# com todas as letras minúsculas, quantas letras ao todo(sem contar os espaços) e quantas letras tem o primeiro nome
nome = str(input('Digite seu nome: '))

qtde_letras = len(nome)
print(f'Seu nome tem {qtde_letras} caracteres')
print(f'{nome} em Maiúsculas = {nome.upper()}')
print(f'{nome} em Minúsculas = {nome.lower()}')
dividido = nome.split()
print(f'Seu primeiro nome tem {len(dividido[0])}, letras')
