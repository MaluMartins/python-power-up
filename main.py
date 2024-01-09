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
import numpy
import openpyxl

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# atalho -> pyautogui.hotkey
# scroll -> pyautogui.scroll

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

#esperar 5 segundos após o enter
time.sleep(5)

# clicar no campo email
pyautogui.click(x=544, y=359)

# digitar email
pyautogui.write("malu@malu.com")

# passar de campo
pyautogui.press("tab")

# digitar senha
pyautogui.write("senha")

pyautogui.press("tab")
pyautogui.press("enter")

# importar a base de dados
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=693, y=240)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preço
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    
    if not pd.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)