'''Crie um arquivo chamado nomes.txt que permita que o usuário
faça a inserção de 10 nomes. Procure no arquivo o arquivo o nome ‘gisele’
'''

arquivo = open('C:\\Users\\ADS\\PycharmProjects\\prof_Gisele\\ex_Gisele\\nomes.txt','w')

for i in range(10):
    nome=input("{0} - digite um nome a ser adicionado: ".format(i+1))
    arquivo.write(nome+"\n")

arquivo.close()

cont=1


arquivo = open("C:\\Users\\ADS\\PycharmProjects\\prof_Gisele\\ex_Gisele\\nomes.txt", "r")

for linha in arquivo:

    if "gisele" in linha:
        linha=linha.replace("\n", "")
        print("o nome {0} foi encontrdo na linha: {1}".format(linha,cont))
    else:
        cont+=1


arquivo.close()



