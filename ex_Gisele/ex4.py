'''Faça a tabuada de 1 até 10 e salve cada uma em um arquivo,
 depois leia e mostre na tela'''
num = 0
for i in range(1, 11):
    arquivo = open("C:\\Users\\ADS\\PycharmProjects\\prof_Gisele\\ex_Gisele\\tabuada" + str(i)+".txt", 'w')
    for j in range(1,11):
        num = i*j
        arquivo.write(str(num))
        arquivo.write("\n")
    arquivo.close()


