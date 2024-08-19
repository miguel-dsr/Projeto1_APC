palavraEscolhidatexto1 = input()
textão = 'açdlkjfasldkjfalsçdkfj 00/batata/00 01/miguel/01 02/fim/02 47/feijão/47alsdkfhaslkdhflaçdfasdfa 03/Hugo Souza/03'
textão2 = 'asklhdasd 00/bacon/00 01/leugim/01 02/começo/02 asddasdfasdfasdçkj 03/melhor goleiro do brasil/03lkgjasd 47/arroz/47'
indexBatata = textão.find(palavraEscolhidatexto1)# acha a posição da palavra escolhida
numeraçãoString = textão[indexBatata - 3:indexBatata - 1]# guarda a numeração da string nesse caso é 0
localMarcaçãoT2 = textão2.find('{}/'.format(numeraçãoString)) # acha a numeração da string no texto 2
indexBatata2 = localMarcaçãoT2 + 3#len('{}/'.format(numeraçãoString))Poderia ser usado mas como a mmarcação vai até dois digitos é mais simples somar 3 # acha a posição de inicio da frase correspondente no texto 2
fimBatata2 = textão2.find('/{}'.format(numeraçãoString))# acha o fim da citação por meio da marcação feita com numero da string /
print(numeraçãoString)
print(fimBatata2)
print(indexBatata)
print(indexBatata2)
print(textão2[indexBatata2:fimBatata2])# mensagem inteira