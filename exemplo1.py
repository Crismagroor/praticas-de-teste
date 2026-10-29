from selenium import webdriver
from selenium.webdriver.common.by import By
import time

drive = webdriver.Chrome()
drive.get("https://ifrs.edu.br/restinga/")
camposPesquisa = drive.find_element(By.ID,"search-field")
camposPesquisa.send_keys("Teste de Software")
camposPesquisa.submit()

print("Titulo do site:", drive.title)

time.sleep(10)

drive.quit