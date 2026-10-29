from selenium import webdriver
from selenium.webdriver.common.by import By
import time

drive = webdriver.Chrome()
drive.get("http://127.0.0.1:5500/usuarios.html")
campoNome  = drive.find_element(By.ID, "nome")
campoEmail = drive.find_element(By.ID, "email")
botao      = drive.find_element(By.ID, "botaoSalvar")

campoNome.send_keys("Maria do exemplo")
campoEmail.send_keys("maria@exemplo.com")
time.sleep(3)
botao.click()
corpoTabela = drive.find_element(By.ID, "userList")
print(corpoTabela.get_attribute("innerHTML"))
linhas = drive.find_elements(By.TAG_NAME, "tr")
linhaInserida = linhas[-1]
print(linhaInserida.get_attribute("innerHTML"))
celulas = linhaInserida.find_elements(By.TAG_NAME, "td")
print(celulas[0].text)
print(celulas[1].text)
print(celulas[2].text)
time.sleep(3)

celulas2 = drive.find_elements(By.CSS_SELECTOR, "#userList tr:last-child td")
print(celulas2[0].text)
print(celulas2[1].text)
print(celulas2[2].text)
drive.quit()
