import re

class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf

    def __str__(self):
        return self.cpf

    def clean_cpf(self):
        self.cpf = re.sub('[^0-9]', '', self.cpf)

    def is_sequence(self):
        memoria = []
        index = 0
        sequence = 1
        for c in self.cpf:
            memoria.append(c)
            if index > 0 and memoria[index] == memoria[index-1]:
                sequence+=1
            index+=1
        if sequence == 11:
            return True
        else:
            return False

    def cpf_valido(self):
        primeira_etapa_de_validacao = 10
        soma_primeira_etapa = 0
        segunda_etapa_de_validacao = 11
        soma_segunda_etapa = 0

        if len(self.cpf) == 11:
            cpf_armazenado = []
            for i in self.cpf:
                cpf_armazenado.append(i)

                if primeira_etapa_de_validacao > 1:
                    soma_primeira_etapa += int(i) * primeira_etapa_de_validacao
                    primeira_etapa_de_validacao -= 1

                if segunda_etapa_de_validacao > 1:
                    soma_segunda_etapa += int(i) * segunda_etapa_de_validacao
                    segunda_etapa_de_validacao -= 1

            validacao1 = soma_primeira_etapa*10 % 11
            validacao2 = soma_segunda_etapa*10 % 11

            if validacao1 == 10:
                validacao1 = 0
            if validacao2 == 10:
                validacao2 = 0

            if validacao1 == int(cpf_armazenado[9]) and validacao2 == int(cpf_armazenado[10]):
                return True