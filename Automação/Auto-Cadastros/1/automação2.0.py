import pandas as pd
import pyautogui as pag
from time import sleep
from unidecode import unidecode

planilha = pd.read_excel('produtos_ficticios2.xlsx', sheet_name='Produtos')
pag.PAUSE = 0.4

for linha in planilha.index:
     pag.click(238,263, duration=1)
     pag.write(unidecode(planilha.loc[linha, 'Nome do produto']))
     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'Descrição']))
     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'Categoria']))
     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'Código do produto']))
     pag.press('tab')
     pag.write(str(planilha.loc[linha, 'Peso (em kg)']))
     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'Dimensões (L x A x P)'])) 
     pag.press('tab')
     pag.press('enter')
     sleep(5)

     pag.press('tab')
     pag.write(str(planilha.loc[linha, 'Preço']))
     pag.press('tab')
     pag.write(str(planilha.loc[linha, 'Quantidade em estoque']))
     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'Data de validade']))
     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'Cor']))

     pag.press('tab')
     pag.press('space')
     tamanho = unidecode(planilha.loc[linha, 'Tamanho'])
     if tamanho == 'Pequeno':
          pag.press('enter')
     elif tamanho == 'Medio':
          pag.press('down')
          pag.press('enter')
     elif tamanho == 'Grande':
          pag.press('down')
          pag.press('down')
          pag.press('enter')
     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'Material']))
     pag.press('tab')
     pag.press('enter')
     sleep(5)

     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'Fabricante']))
     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'País de origem']))
     pag.press('tab')
     observacao = unidecode(planilha.loc[linha, 'Observações'])
     if observacao != 'Nenhuma':
          pag.write(observacao)
     pag.press('tab')
     pag.write(str(planilha.loc[linha, 'Código de barras']))
     pag.press('tab')
     pag.write(unidecode(planilha.loc[linha, 'Localização no armazém']))
     pag.press('tab')
     pag.press('enter')
     sleep(4)
     pag.click(917,177)
     sleep(4)
     pag.click(743,536)
