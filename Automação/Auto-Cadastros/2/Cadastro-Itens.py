import pyautogui as pag
import pandas as pd
import time
pag.PAUSE = 0.4


# abrir chrome

pag.click(x=669, y=751)

# acessar site

pag.click(x=294, y=61)
pag.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pag.press('enter')
time.sleep(5)

# logar

pag.press('tab')
pag.write('nykorod')
pag.press('tab')
pag.write('nykorodélindao')
pag.press('tab')
pag.press('enter')
time.sleep(3)

# cadastrar item
tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    pag.click(x=414, y=284)
    pag.write(str(tabela.loc[linha, 'codigo']))
    pag.press('tab')
    pag.write(str(tabela.loc[linha, 'marca']))
    pag.press('tab')
    pag.write(str(tabela.loc[linha, 'tipo']))
    pag.press('tab')
    pag.write(str(tabela.loc[linha, 'tipo']))
    pag.press('tab')
    pag.write(str(tabela.loc[linha, 'preco_unitario']))
    pag.press('tab')
    pag.write(str(tabela.loc[linha, 'custo']))
    pag.press('tab')
    obs = (str(tabela.loc[linha, 'obs']))
    if obs != 'nan':
        pag.write(obs)
    pag.press('tab')
    pag.press('enter')
    pag.scroll(3000)


