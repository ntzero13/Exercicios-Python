listaseven = [1,2,3,4,5,6,7]
listavazia = [ ]
meu_setvazio = [ ] 
meu_set2 = [1,4,6,5,7,2,3]
tupla = ()
tupla2 = 1,2,3,4,5,6,7
dic_vazio = { }
dic_notas = {'joao': 10, "maria": 2,"ricardo": 3,"manoel": 8,"Eduardo": 20}


def menu_():
    opcao=1

    while opcao:
        print("0. Sair")
        print("1. inserir valor na lista com 7 elementos")
        print("2. inserir valor na lista vazia")
        print("3. inserir valor no set vazio")
        print("4. inserir valor no set com 7 elementos ")
        print("5. inserir valor no tuplo vazio ")
        print("6. inserir valor no tuplo com 7 elementos ")
        print("7. inserir valor no dicionario vazio ")
        print("8 inserir valor no dicionario com 5 elementos")
        opcao = int(input("Opção: "))

        if(opcao==1):
            ans = []
            n = int(input("Enter number of elements : "))
            for i in range(0, n):
                x= (input('Adicione valor na lista: '))
                ans.append(x)
            ans.extend(listaseven)    
            print (ans)
                
                

        if(opcao==2):
            b2b = []
            a = int(input("Enter number of elements : "))
            for i in range(0, a):
                y= (input('Adicione valor na lista: '))
                b2b.append(y)
            b2b.extend(listavazia)
            print (b2b)

        if(opcao==3):
            sett_ = []
            b = int(input("Enter number of elements : "))
            for i in range(0, b):
                z= (input('Adicione valor na set vazia: '))
                sett_.append(z)
            sett_.extend(meu_setvazio)
            set_destinos = set(sett_)
            print (set_destinos)

        if(opcao==4):
            sett_2 = []
            c = int(input("Enter number of elements : "))
            for i in range(0, c):
                w = (input('Adicione valor na set com 7 elementos: '))
                sett_2.append(w)
            sett_2.extend(meu_set2)
            set_destinos2 = set(sett_2)
            print (set_destinos2)

        if(opcao==5):
            tupl_ = []
            d = int(input("Enter number of elements : "))
            for i in range(0, d):
                t= (input('Adicione valor na tuple vazia: '))
                tupl_.append(t)
            tupl_.extend(tupla)
            print (tupl_)

        if(opcao==6):
            tupl_a = []
            e = int(input("Enter number of elements : "))
            for i in range(0, e):
                zb= (input('Adicione valor na tuplo com 7 elementos: '))
                tupl_a.append(zb)
            tupl_a.extend(tupla2)
            print (tupl_a)

        if(opcao==7):
            nome1 = input("Digite o nome do aluno: ")
            nota1 = input("Nota dele: ")

            if dic_vazio.get(nome1):
                print("Ja existe o aluno ",nome1)
            else:
                dic_vazio[nome1] = nota1
                print(dic_vazio) 

        if(opcao==8):
            dic_nvazias = {}
            nome = input("Digite o nome do aluno: ")
            
            if dic_notas.get(nome):
                print("Ja existe o aluno ",nome)
                print(dic_notas)
            else:
                nota = input("Nota dele: ")
                dic_nvazias = dic_notas.copy()
                dic_nvazias[nome] = nota
                print(dic_nvazias)            
                
                
                

menu_()