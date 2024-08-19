palavraEscolhidatexto1 = input()
textão = 'açdlkjfasldkjfalsçdkfj 0/batata/0 1/miguel/1 2/fim/2 alsdkfhaslkdhflaçdfasdfa'
textão2 = 'asklhdasd 0/bacon/0 1/leugim/1 2/começo/2 asddasdfasdfasdçkjlkgjasd'
indexBatata = textão.find(palavraEscolhidatexto1)# acha a posição da palavra escolhida
numeraçãoString = textão[indexBatata - 2]# guarda a numeração da string nesse caso é 0
localMarcaçãoT2 = textão2.find('{}/'.format(numeraçãoString)) # acha a numeração da string no texto 2
indexBatata2 = localMarcaçãoT2 + 2# acha a posição de inicio da frase correspondente no texto 2
fimBatata2 = textão2.find('/{}'.format(numeraçãoString))# acha o fim da citação por meio da marcação feita com numero da string /
print(indexBatata)
print(indexBatata2)
print(textão2[indexBatata2:fimBatata2])# mensagem inteira