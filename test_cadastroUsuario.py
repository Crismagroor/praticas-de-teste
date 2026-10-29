import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope = "session")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5501/usuarios.html")
    yield driver
    driver.quit()
def test_cadastro(driver):
    campoNome = driver.find_element(By.ID, "nome")
    campoEmail = driver.find_element(By.ID, "email")
    campoNome.send_keys("Maria do exemplo")
    campoEmail.send_keys("teste@exemplo.com")
    botao = driver.find_element(By.ID, "botaoSalvar")
    botao.click()
    celulas2 = driver.find_elements(By.CSS_SELECTOR, "#userList tr:last-child td")
    assert celulas2[1].text == "Maria do exemplo"
    assert celulas2[2].text == "teste@exemplo.com"

def test_excluir(driver):
    campoNome = driver.find_element(By.ID, "nome")
    campoEmail = driver.find_element(By.ID, "email")
    campoNome.send_keys("Maria do exemplo")
    campoEmail.send_keys("teste@exemplo.com")
    botao = driver.find_element(By.ID, "botaoSalvar")
    botao.click()
    celulas2 = driver.find_elements(By.CSS_SELECTOR, "#userList tr:last-child td")
    id = celulas2[0].text
    botoes =  celulas2[3].find_elements(By.TAG_NAME, "button")
    botoes[1].click()
    celulasDepoisExclusao = driver.find_elements(By.CSS_SELECTOR, "#userList tr:last-child td")
    assert len(celulasDepoisExclusao) == 0 or id!= celulasDepoisExclusao[0].text
def test_editar(driver):
    botoes = driver.find_elements(By.CSS_SELECTOR,"#userList tr:last-child button")
    botoes[0].click()
    campoNome = driver.find_element(By.ID, "nome")
    campoEmail = driver.find_element(By.ID, "email")
    campoNome.clear()
    campoNome.send_keys("Maria do exemplo")
    campoEmail.clear()
    campoEmail.send_keys("teste@exemplo.com")
    botao = driver.find_element(By.ID, "botaoSalvar")
    botao.click()
    celulas2 = driver.find_elements(By.CSS_SELECTOR, "#userList tr:last-child td")
    assert celulas2[1].text == "Maria do exemplo"
    assert celulas2[2].text == "teste@exemplo.com"
