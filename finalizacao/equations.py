from math import pi, pow, sqrt
from constants import Constants
from funcions import truncate


class Equations(Constants):
    def __init__(self):
        super().__init__()
        self.runloop = True
        self.rn = 0
        self.Kn = 0
        self.Un = 0
        self.En = 0
        self.nivelAtual = 1
        self.estadoAtual = 0
        self.series_niveis = {
            1: " - (Série de Lyman)",
            2: " - (Série de Balmer)",
            3: " - (Série de Paschen)",
            4: " - (Série de Brackett)",
            5: " - (Série de Pfund)"
        }
        self.options = [
            [0, 1, 2, 3],  # Menu princpal
            [0, 1, 2, 3, 4],  # Menu aula 1
            [0, 1, 2, 3, 4, 5, 6],  # Menu aula 2
            [0, 1]  # Menu aula 3
        ]
        self.messages = [
            "======================== PROJETO 3 ========================\n"
            "0- Sair\n"
            "1- Cálculos de energia e raio de um átomo de hidrogênio\n"
            "2- Estudo das séries de Lyman, Balmr, Paschen, Brackett e Pfund\n"
            "3- Absorção ou emissão de um fóton por um átomo de hidrogênio\n",

            "Escolha a opção desejada:\n"
            "0- Voltar\n"
            "1- Calcular o raio da órbita\n"
            "2- Calcular a energia cinética do elétron\n"
            "3- Calcular a energia potencial do elétron\n"
            "4- Calcular a energia total do átomo de hidrogênio\n",

            "Escolha a opção desejada:\n"
            "0- Voltar\n"
            "1- Série de Lyman (n = 1)\n"
            "2- Série de Balmer (n = 2)\n"
            "3- Série de Paschen (n = 3)\n"
            "4- Série de Brackett (n = 4)\n"
            "5- Série de Pfund (n = 5)\n"
            "6- Outros número quântico inicial e final\n",

            "Escolha a opção desejada:\n"
            "0- Voltar\n"
            "1- Calcular nível final do elétron\n",
        ]

    def loop(self):

        print()
        print(self.messages[self.estadoAtual])
        op = 100
        input_loop = True

        while input_loop:
            check = False
            try:
                op = int(input("> "))
                input_loop = False
            except ValueError:
                print("Opção inválida! Tente novamente.")
                check = True
            finally:
                if not check:
                    if op < 0 or op not in self.options[self.estadoAtual]:
                        print("Opção inválida! Tente novamente.")
                        input_loop = True
            print()

        if self.estadoAtual == 0:  # Menu principal
            if op == 0:
                self.runloop = False
                print("...Tenha um bom dia!")
            else:
                self.estadoAtual = op

        elif self.estadoAtual == 1:  # Menu com as questões da aula 1

            if op == 0:
                self.estadoAtual = 0
                print()
            else:
                n = self.get_numero_quantico(1, "")

                if op == 1:
                    self.raio_orbita(n)
                elif op == 2:
                    self.enrgia_cinetica_eletron(n)
                elif op == 3:
                    self.energia_potencial_eletron(n)
                elif op == 4:
                    self.energia_total_eletron(n)

        elif self.estadoAtual == 2:  # Menu com as questões da aula 2
            if op == 0:
                self.estadoAtual = 0
                print()

            else:
                comprimento = 0
                n_inicial = 0
                n_final = 0

                if 1 <= op <= 5:
                    limite = op + 1
                    self.nivelAtual = op
                    n_inicial = self.get_numero_quantico(limite, "inicial")
                    n_final = op
                else:
                    n_inicial = self.get_numero_quantico(1, "inicial")
                    n_final = self.get_numero_quantico(1, "final")
                    self.nivelAtual = n_final

                    if n_inicial > n_final:
                        temp = n_inicial
                        n_inicial = n_final
                        n_final = temp

                comprimento = self.comprimento_de_onda_do_eletron(n_final, n_inicial)

                if comprimento < 0:
                    comprimento *= -1

                print()
                print("Comprimento de onda do elétron durante a transição é {} m".format(comprimento))

                if self.nivelAtual == 2:
                    cor = self.get_cor_da_onda(comprimento)
                    print("Cor do elétron durante a a transição é {}".format(cor))

        elif self.estadoAtual == 3:  # Menu com as questões da aula 3

            if op == 0:
                self.estadoAtual = 0
            else:
                self.absorcao_do_foton()

    def absorcao_do_foton(self):
        comprimento = self.get_entrada_comprimento()
        En = self.calcular_energia_pelo_comprimento(comprimento)
        n, ionizou = self.get_nivel_quantico(En, 13.6)

        n_inteiro = float(round(n, 1))
        n_inteiro_mais_1 = int(n_inteiro + 0.1)
        n_inteiro = int(n_inteiro)

        # print("n: {}".format(n))
        # print("n_inteiro: {}".format(n_inteiro))

        if ionizou:
            print("Digite um comprimento de onda maior, esse fóton irá ionizar o átomo de hidrogênio.")
            print()
            return self.absorcao_do_foton()

        elif n_inteiro <= 1:
            print("O átomo de hidrogênio não absorve o fóton com comprimento de onda dado.")

        else:
            # print("n_inteiro_mais_1: {}".format(n_inteiro_mais_1))

            if n_inteiro_mais_1 > n_inteiro:
                n_inteiro = n_inteiro_mais_1
            else:
                n_inteiro = int(n_inteiro)

            # print("n_inteiro_after: {}".format(n_inteiro))

            print("O átomo de hidrogênio absorve o fóton e vai para o nível {}".format(
                n_inteiro), end=" ")

            if n_inteiro in self.series_niveis:
                print("{}".format(self.series_niveis[n_inteiro]), end="")

            print()

        return 0

    def get_numero_quantico(self, limite, tipo):
        n = 0
        try:
            n = int(input("Entre com o valor do número quântico {}: ".format(tipo)))
            if n < limite:
                raise Exception("Nenhum número abaixo de {} permitido.".format(limite))
        except:
            print("Valor digitado inválido.")
            print()
            return self.get_numero_quantico(limite, tipo)

        return n

    def get_entrada_comprimento(self):
        # "Digite o comprimento de onda do fóton que se aproxima do átomo de hidrogênio: "
        loop = True
        comprimento = 1

        while loop:

            entrada = input("Digite o comprimento de onda do fóton que se aproxima do átomo de hidrogênio: ")

            try:
                comprimento = float(entrada)

                if comprimento > 0:
                    loop = False
                else:
                    print("Valor inválido! Tente novamente.")
                    print()

            except ValueError:
                print("Valor inválido! Tente novamente.")
                print()

        return comprimento

    def calcular_energia_pelo_comprimento(self, comprimento):
        # En = (h*c) / comprimento
        En = (((self.planck_constant / self.elementary_charge) * 3e8) / comprimento)
        # En = (((6.626e-34 / 1.602e-19) * self.light_speed) / comprimento)
        # ("energia: {} eV".format(En))
        return En

    def get_nivel_quantico(self, energia_final, energia_inicial):
        ionizou = False

        # delta = energia_inicial - energia_final
        # n² = -13.6 / -delta

        # print("Ei = {}\nEf = {}".format(energia_inicial, energia_final))
        delta = energia_final - energia_inicial
        # print("delta: {} eV".format(delta))

        if delta > 0:
            ionizou = True

        elif delta < 0:
            delta *= -1

        n = sqrt((-13.6 / -delta))
        # print("nivel: {}".format(n))

        return n, ionizou

    def comprimento_de_onda_do_eletron(self, n_final, n_inicial):
        deltaN = ((1 / (n_final * n_final)) - (1 / (n_inicial * n_inicial)))
        comprimento = 1 / (self.rydberg_constant * deltaN)
        return comprimento

    def get_cor_da_onda(self, comprimento):
        # ultravioleta, violeta, azul, verde, vermelho, infravermelho
        limites = [
            364.6e-9,  # 0
            410.2e-9,  # 1
            434.1e-9,  # 2
            486.1e-9,  # 3
            656.3e-9,  # 4
        ]
        cores = [
            "ultra-violeta",  # 0
            "violeta",  # 1
            "azul",  # 2
            "verde",  # 3
            "vermelho",  # 4
            "infra-vermelho"  # 5
        ]

        indice = 0
        if comprimento < limites[0]:
            # print("if1")
            indice = 0
        elif comprimento > limites[4]:
            # print("if2")
            indice = 4
        else:
            # print("else")
            if limites[0] <= comprimento < limites[1]:
                # print("if3")
                indice = 0
            elif limites[1] <= comprimento < limites[2]:
                # print("if4")
                indice = 1
            elif limites[2] <= comprimento < limites[3]:
                # print("if5")
                indice = 2
            elif limites[3] <= comprimento <= limites[4]:
                # print("if6")
                indice = 3

        # print("indice: {}".format(indice))

        return cores[indice]

    def raio_orbita(self, n):
        self.rn = self.electric_constant * ((pow(n, 2) * pow(self.planck_constant, 2)) / (
                pi * self.electron_mass * pow(self.elementary_charge, 2)))
        print("Raio: {}".format(self.rn))

    def enrgia_cinetica_eletron(self, n):
        self.Kn = 13.60 / pow(n, 2)
        print("Energia cinetica do elétron: {}".format(self.Kn))

    def energia_potencial_eletron(self, n):
        self.Un = -27.20 / pow(n, 2)
        print("Energia potencial do elétron: {}".format(self.Un))

    def energia_total_eletron(self, n):
        self.En = -13.60 / pow(n, 2)
        print("Energia total do elétron: {}".format(self.En))
