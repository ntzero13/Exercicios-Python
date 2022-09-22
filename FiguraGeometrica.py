import math

class figuraGeometrica:
    
    def __init__(self):
        print("Figura Geometrica")
    
    def area(self):
        pass

    def perimetro(self):
        pass

class quadrado(figuraGeometrica):
        
    def __init__(self,lado):
       
        self.lado = lado 

    def area(self):
        print(self.lado * self.lado)
    
    def perimetro(self):
        print(self.lado * 4)
    
class retangulo(figuraGeometrica):
    
    def __init__(self):
            c = float(input('Digite o valor do lado do Retangulo: '))
            b = float(input('Digite o valor da base do retangulo: '))
            self.b = b
            self.c = c
    def area(self):
        return self.b * self.c / 2
        
class circulo(figuraGeometrica):
        
    def __init__(self, raio):
            self.raio = raio

    def area(self):
        return self.raio * self.raio * 3.14

class triangulo(figuraGeometrica):
    def __init__(self,lado_):
        lado_ = float(input('Digite o valor dos lados do Triangulo: '))
        self.lado_ = lado_ 

    def calc_perimetro(self):
        return self.lado_ * 3 
    

def menu():
    escolha=True
    while escolha:
        print("\n")
        print("Calcular Areas e Perimetros")
        print("""
        1.Calcular àrea e o perimetro do triângulo
        2.Calcular àrea e o perimetro do quadrado
        3.Calcular àrea e o perimetro do retângulo
        4.Calcular àrea e o perimetro do círculo
        5.Exit/Quit/Saída
        """)
        escolha= input("Escolha uma opção:  ")
        if escolha=="1":
            print('\n')
            triangulo()

        elif escolha=="2":
            print('\n')
            x = quadrado(10)
            x.area()
            
            print('O resultado do calculo da area é:', x )

        elif escolha=="3":
            print('\n')
            retangulo()
        elif escolha == "4":
            print('\n')
            x = circulo()
            x.area()
        elif escolha=="5":
            print("\n Adeus")
            escolha = None
        else:
            print("\n Escolha não válida.\n Tente outra vez.")

menu()

