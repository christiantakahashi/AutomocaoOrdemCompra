import pyautogui
import time
import pandas as pd  # Para baixar jogue no terminal 'pip install pandas openpyxl'

# =CONCATENAR(F8;",";I8;",";H8;",";L8) codigo excel 

tabela = pd.read_csv("PlacasFicticias.csv")

print(tabela)

# Passo 1: Incluir serviço na ordem de compra
for linha in tabela.index:
    pyautogui.click(x=212, y=347) # INCLUIR
    # clicar no campo de código
    pyautogui.click(x=853, y=486)
    pyautogui.click(x=853, y=486) # DUBLE CLICLK      
    # pegar da tabela o valor do campo que a gente quer preencher
    Placa = tabela.loc[linha, "PLACA"]
    time.sleep(0.8)
    # preencher o campo
    pyautogui.write(str(Placa))
    time.sleep(0.8)
    # passar para o proximo campo
    pyautogui.click(x=310, y=409)
    time.sleep(0.8)
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "CODIGO"]))
    time.sleep(0.8)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "VOLUME"]))
    time.sleep(0.8)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "VALOR"]))
    time.sleep(0.8)
    pyautogui.click(x=367, y=346) # cadastra o serviço (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim