import PySimpleGUI as sg
from time import sleep 
sg.theme('reddit')

login=[
     [sg.Text('cpf')],
     [sg.Input(key='usuario')],
     [sg.Text('senha')],
     [sg.Input(password_char='*', key= 'senha')],
     [sg.Button('salvar')],
     [sg.Output(size=(43,10))]
]
janela = sg.Window('Principal', layout=login)
while True:
     event, values= janela.read()
     if event == sg.WIN_CLOSED:
          break
     elif event == 'salvar':
          usuario = values['usuario']
          senha = values['senha']
          print('passo 1: completo')
          sleep(2)
          print('passo 2: completo')
          sleep(2)
          print('passo 3: completo')
          sleep(2)