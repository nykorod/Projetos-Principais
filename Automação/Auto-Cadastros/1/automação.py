import openpyxl as op
import pyperclip as pp
import pyautogui as pag
from time import sleep

planilha = op.load_workbook('produtos_ficticios.xlsx')
sheetProdutos = planilha['Produtos']
sleep(2)
for linha in sheetProdutos.iter_rows(min_row=2):
     
     produtoNome = linha[0].value
     pp.copy(produtoNome)
     pag.click(238,263, duration=1)
     pag.hotkey('ctrl', 'v')

     produtoDescricao = linha[1].value
     pp.copy(produtoDescricao)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')

     produtoCategoria = linha[2].value
     pp.copy(produtoCategoria)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')

     produtoCodigo = linha[3].value
     pp.copy(produtoCodigo)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')

     produtoPeso = linha[4].value
     pp.copy(produtoPeso)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     produtoDimensoes = linha[5].value
     pp.copy(produtoDimensoes)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     pag.press('tab')
     pag.press('enter')
     sleep(3)

     produtoPreco = linha[6].value
     pp.copy(produtoPreco)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     produtoEstoque = linha[7].value
     pp.copy(produtoEstoque)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     produtoValidade = linha[8].value
     pp.copy(produtoValidade)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     produtoCor = linha[9].value
     pp.copy(produtoCor)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     produtoTamanho = linha[10].value
     pag.press('tab')
     pag.press('space')
     if produtoTamanho == 'Pequeno':
          pag.press('enter')
     elif produtoTamanho == 'Médio':
          pag.press('down')
          pag.press('enter')
     elif produtoTamanho == 'Grande':
          pag.press('down')
          pag.press('down')
          pag.press('enter')

     produtoMaterial = linha[11].value
     pp.copy(produtoMaterial)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     pag.press('tab')
     pag.press('enter')
     sleep(3)     

     produtoFabricante = linha[12].value
     pp.copy(produtoFabricante)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     produtoOrigem = linha[13].value
     pp.copy(produtoOrigem)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     produtoObservacoes = linha[14].value
     pp.copy(produtoObservacoes)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     produtoCodigoBarras = linha[15].value
     pp.copy(produtoCodigoBarras)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     produtoArmazem = linha[16].value
     pp.copy(produtoArmazem)
     pag.press('tab')
     pag.hotkey('ctrl', 'v')
     pag.press('tab')
     pag.press('enter')
     sleep(2)
     pag.click(917,177)
     sleep(2)
     pag.click(743,536)


