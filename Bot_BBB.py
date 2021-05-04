"""
Robô para votação do BBB
Criação: ETLS em 01/05/2021

Requisitos:

• Ter o python instalado na sua máquina.

• Site do gshow ja deve esta logada na página da votação.

• Saber a posição da tela onde o mouse deve ser clicado. A posição mudará de acordo com a posição do candidato na tela.
    Para isso use o método PosicaoMouse() e mude a posição no método votar(). (código pronto no final do script)
    Nesse exemplo (são três candidatos no paredão) o candidato a ser votado esta no meio dos outros dois (posição 662, 343).
    
• Vote pelo menos uma vez manualmente, para então, executar o robo.
"""


from ProcessosWin import Processos
import pyautogui
import time

class Robo_BBB:
    
    def __init__(self):
        """ variaveis iniciais e atribuição da classe Processos. """
        
        self.nomeproc = 'Paredão BBB21:'
        self.botprocessos = Processos(self.nomeproc)
        self.qtd_inicial = 0
        self.qtd_votos = 1000000000
        
    def ChamarTelaVotacao(self):
        """ Função para chamar a tela de votação do BBB para primeiro plano. """
        
        self.botprocessos.BrowserPrimeiroPlano()
        
    def PosicaoMouse(self):
        """ Função para saber a possição do mouse.
        
        A posição dos itens de votação pode variar conforme a tela.
        """
        
        pmouse = pyautogui.position()
        pyautogui.alert(pmouse)
        print(pmouse)
                
    def votar(self):
        """ Função que realizará a votação em um loop."""
        
        while self.qtd_inicial < self.qtd_votos:
            """ caso a internet esteja lenta, aumente os segundos do time.sleep() """
            time.sleep(1)
            pyautogui.press('pagedown')
            time.sleep(1)
            pyautogui.click(662, 343) # clicar na posicao do participante escolhido
            time.sleep(5)
            pyautogui.press('tab') # ir para a caixinha do "sou humano"
            time.sleep(1)
            pyautogui.press('enter') # clicar enter
            time.sleep(15)
            pyautogui.press('pagedown')
            time.sleep(1)
            pyautogui.click(668, 380) # clicar em "votar novamente"
            time.sleep(5)
            self.qtd_inicial = self.qtd_inicial + 1
        return self.qtd_inicial


""" =========== Programa Principal =========== """
try:
    bbb = Robo_BBB() # Instanciando a classe Processos
    # chamando módulos
    bbb.ChamarTelaVotacao()
    execucao = bbb.votar()
except:
    pyautogui.alert('Erro na execução')
finally:
    pyautogui.alert('Foram executados {} votos'.format(execucao))
    # import os
    # os.system('pause')


""" Use essa Parte do Código para descobrir a posição do mouse (comente a parte do Programa Principal e descomente essa parte aqui) """
# bbb = Robo_BBB()
# bbb.PosicaoMouse()