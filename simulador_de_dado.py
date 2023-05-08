# Simulador de dado
# Simular o uso de um dado gerando um valor de 1 até 6.

import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minino = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
        # layout
        layout =  [
                


        ]
        # criar uma janela
        # ler os valores da tela
        # fazer alguma coisa com esses valores


    def Iniciar(self):
        try:
            resposta = input(self.mensagem)
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta.')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minino, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()