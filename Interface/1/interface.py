import PySimpleGUI as sg
sg.theme('reddit')

Layout = [
     [sg.Text('E-mail'), sg.Input(key= 'Email')],
     [sg.Text('Senha'), sg.Input(key = 'Senha', password_char='*')],
     [sg.FolderBrowse('Escolher Pasta Anexos',target='input_anexos'),sg.Input(key='input_anexos')],
     [sg.FolderBrowse('Escolher Pasta Planilha',target='input_planilha'),sg.Input(key='input_planilha')],
     [sg.Button('Salvar')]
]

janela = sg.Window('Principal', layout=Layout)

while True:
     event, values= janela.read()
     if event == sg.WIN_CLOSED:
          break
     elif event == 'Salvar':
          email = values['Email']
          senha = values['Senha']
          anexo = values['input_anexos']
          planilha = values['input_planilha']
          print(f'email: {email}')
          print(f'senha: {senha}')
          print(f'anexo: {anexo}')
          print(f'planilha: {planilha}')
          

# logar mo email
     # email
     # senha
# lugar para anexos
     # escolher pasta
# lugar para qr code
     # escolher pasta
# salvar
