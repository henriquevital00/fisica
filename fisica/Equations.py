from Constants import Constants
from math import pow
from math import pi


class Equations(Constants):
    def __init__(self):
        super().__init__()
        self.rn = 0
        self.Kn = 0
        self.Un = 0
        self.En = 0

    def message(self):
        print("Digite o numero correspondente a opção de calculo desejada:")
        print("1- Calcular o raio da órbita")
        print("2- Calcular a energia cinética do elétron")
        print("3- Calcular a energoa potencial do elétron")
        print("4- Calcular a energia total do átomo de hidrogenio")
        op = int(input())
        while (op not in [1, 2, 3, 4]):
            print("Valor digitado incorreto")
            op = int(input("Digite a opção novamente: "))
        try:
            n = int(input("Entre com o valor de n: "))
        except:
            print("Numero digitado incorreto")
            n = int(input("Entre com o valor novamente: "))
        if (op == 1):
            self.raio_orbita(n)
        elif (op == 2):
            self.enrgia_cinetica_eletron(n)
        elif (op == 3):
            self.energia_potencial_eletron(n)
        elif (op == 4):
            self.energia_total_eletron(n)

    def raio_orbita(self, n):
        self.rn = self.electric_constant*((pow(n, 2) * pow(self.planck_constant, 2)) / (pi * self.eletron_mass * pow(self.elementary_charge, 2)))
        print("Raio: " + str(self.rn))

    def enrgia_cinetica_eletron(self, n):
        self.Kn = 13.60 / pow(n, 2)
        print("Energia cinetica do eletron: " + str(self.Kn))

    def energia_potencial_eletron(self, n):
        self.Un = -27.20 / pow(n, 2)
        print("Energia potencial do eletron: " + str(self.Un))

    def energia_total_eletron(self, n):
        self.En = -13.60 / pow(n, 2)
        print("Energia total do eletron: " + str(self.En))
