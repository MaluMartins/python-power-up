# passo a passo da automação:

# 1 - entrar no sistema da empresa:
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# libs em python

# 2 - fazer login no sistema
# 3 - importar a base de dados
# 4 - cadastrar um produto
# 5 - repetir o cadastro dos produtos até acabar a base de dados

import pyautogui
import time
import pandas as pd

def descobrir_posicao():
    time.sleep(5)
    return pyautogui.position()

def acessar_site():
    pyautogui.PAUSE = 2
    # apertar a tecla windows
    pyautogui.press("win")

    # digitar o nome do programa (chrome)
    pyautogui.write("edge")

    # apertar enter
    pyautogui.press("enter")

    # digitar o link
    link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    pyautogui.write(link)

    pyautogui.press("enter")

def login():
    pyautogui.PAUSE = 0.5
    # clicar no campo email
    posicao = descobrir_posicao()
    pyautogui.click(posicao)

    # digitar email
    pyautogui.write("malu@malu.com")

    # passar de campo
    pyautogui.press("tab")

    # digitar senha
    pyautogui.write("senha")

    pyautogui.press("tab")
    pyautogui.press("enter")

# importar a base de dados
tabela_produtos = pd.read_csv("produtos.csv")

# print(list(tabela_produtos.columns))

def preencher_form():
    pyautogui.PAUSE = 0.5
    posicao = descobrir_posicao()

    for linha in tabela_produtos.index:
        pyautogui.click(posicao)
        for coluna in tabela_produtos.columns:
            
            valor = tabela_produtos.loc[linha, coluna]

            if not pd.isna(valor):
                pyautogui.write(str(valor))

            pyautogui.press("tab")  
            pyautogui.press("enter")

            pyautogui.scroll(5000)

acessar_site()
time.sleep(2)
login()
time.sleep(2)   
preencher_form()