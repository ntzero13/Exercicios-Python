myList = [1,3,2,4,3,1,0,9,7,2,4,5,6]
lista = 0
def soma_elementos(total):
    total = 0
    for i in myList:
        total += i
    somatotal = total
    return somatotal

total_ = soma_elementos(myList);
print ("A soma de todos os valores da lista é: ", total_)

def contarElementos(count):
    count = 0
    for element in myList:
        count += 1
    contagemfinal = count
    return contagemfinal

contaTotal = contarElementos(myList);
print ("O total da contagem dos elementos dentro da lista é: ",contaTotal)

repitido = [x for i, x in enumerate(myList) if i != myList.index(x)]
print("O primeiro valor repitido é: ",repitido[0])