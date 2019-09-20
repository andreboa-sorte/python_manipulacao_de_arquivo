'''Faça um programa que crie um arquivo contendo o nome de 5 pessoas,
se o nome informado for igual ao seu nome crie outro arquivo
somente com o seu nome.'''


arquivo = open('C:\\Users\\ADS\\PycharmProjects\\prof_Gisele\\ex_Gisele\\nomes_ex2.txt','w')

seu_nome = open('C:\\Users\\ADS\\PycharmProjects\\prof_Gisele\\ex_Gisele\\seu_nome.txt','w')

condicao=input("digite o seu nome: ")

for i in range(5):
    nome=input("{0} - digite um nome a ser adicionado: ".format(i+1))
    if nome == condicao:
        seu_nome.write(nome+"\n")
    else:
        arquivo.write(nome+"\n")

arquivo.close()
seu_nome.close()

arquivo = open("C:\\Users\\ADS\\PycharmProjects\\prof_Gisele\\ex_Gisele\\nomes_ex2.txt", "r")
print("a lista de nomes, sem o seu nome: ")
for linha in arquivo:
    print(linha)
arquivo.close()


seu_nome = open("C:\\Users\\ADS\\PycharmProjects\\prof_Gisele\\ex_Gisele\\seu_nome.txt", "r")

print("a lista com o seu nome: ")
for linha in seu_nome:
    print(linha)
seu_nome.close()


