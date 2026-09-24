from random import randint

class Carro:

    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor
        self.distancia = 0

    def percorrer_distancia(self, distancia):
        self.distancia += distancia

def iniciar_jogo():

    ferrari = Carro("Ferrari", "Vermelha")
    porshe = Carro("Porshe", "Preto")
    mustang = Carro("Mustang", "Azul")

    while True:
        ferrari.percorrer_distancia(randint(0, 10))
        porshe.percorrer_distancia(randint(0, 10))
        mustang.percorrer_distancia(randint(0, 10))

        if ferrari.distancia >= 100:
            print(f"o vencedor foi o carro {ferrari.nome} {ferrari.cor}")
            break

        if porshe.distancia >= 100:
                    print(f"o vencedor foi o carro {porshe.nome} {porshe.cor}")
                    break

        if mustang.distancia >= 100:
                    print(f"o vencedor foi o carro {mustang.nome} {mustang.cor}")
                    break
iniciar_jogo()