"""frutas = []

for i in range (4):
    fruta = str(input("Escreva a fruta no qual quer adicionar: "))
    frutas.append (fruta)

    print (frutas)

while True:

    print ("is true")

def soma(x, y):

    x = int(x)
    y = int(y)

    print (x + y)
    return x + y

    resultado = soma(5, 4)

    print (resultado) 

  #capitalização
    
nova_string = "lucas"

capitalizado = nova_string.capitalize()

print (capitalizado)

#onde está a letra

string = "Lucas"

onde_esta_o_l = string.find("L")

#descapitalização

new_string = "LUCAS"

descapitalizando = new_string.lower()

print (descapitalizando)""" 

"""class Carro:

    def __init__(self, marca, modelo, ano):

        self.marca = marca

        self.modelo = modelo

        self.ano = ano

    def ligar(self):

        print ("Seu veículo da marca ", self.marca, "modelo ", self.modelo, "e ano ", self.ano, "ligou")

meu_carro = Carro("Chrevrolet", "Onix", 2020)
meu_carro.ligar()"""

class Animal:

    def __init__(self, especie):

        self.especie = especie

        if especie == "Cachorro":

            print (Cachorro.latir)

    def som(self):
        
        self.latir = "latir"
        
        self.miar = "miar"

class Cachorro(Animal):

    def latir(self):

        return "O ", self.especie, "está a ", self.latir

class Gato(Animal):

    def miar(self):

        return "O ", self.especie, "está a ", self.miar
    
meu_cachorro = Cachorro("Alfredo")

print (meu_cachorro.especie, meu_cachorro.latir)




class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        return ": au au !"

class Gato(Animal):
    def som(self):
        return ": miau"

meu_cachorro = Cachorro("Harry")
print(meu_cachorro.nome, meu_cachorro.som())

