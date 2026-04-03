
#TODO fazer o sistema mais eficiente para enviar fotos
#TODO fazer um forma de enviar mais de uma foto 


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import dotenv
import os

dotenv.load_dotenv(".env.config")

def send(): 
    options = webdriver.ChromeOptions()

    # pegando as opçoes do navegador
    pasta_perfil = os.path.join(os.getcwd(), "chrome-data")  # caminho absoluto
    options.add_argument(f"user-data-dir={pasta_perfil}")

    #abrindo o navegador como driver

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # entrando no whatsapp
    driver.get('https://web.whatsapp.com')

    #encontrando a barra de pesquisa -> clica na barra de pesquisa -> escreve o nome do grupo
    barra_pesquisa = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Pesquisar ou começar uma nova conversa" and @role="textbox"]'))
    )
    barra_pesquisa.click()
    
    nome_do_grupo = os.getenv("nomedogrupo")

    barra_pesquisa.send_keys(f"{nome_do_grupo}")

    #encontra o grupo -> clica no grupo

    grupo =  WebDriverWait(driver,60).until(
        EC.presence_of_element_located((By.XPATH, f'//span[@title="{nome_do_grupo}"]'))
    )
    grupo.click()


    imagem =f'C:/Users/RT/Desktop/trabalhos/codigos em andamento/autoenvzap/{os.getenv("img")}'
    btn_anexar = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Anexar" and @data-tab="10"]'))
    )

    btn_anexar.click()
    file_input = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    file_input.send_keys(imagem)

    time.sleep(3) # Esperar a imagem carregar

    # encontra o botão de enviar - > clica nele
    env = WebDriverWait(driver,30).until(
        EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="Enviar" and @role="button"]'))
    )
    env.click()

    # espera enviar a imagem -> sai do programa
    time.sleep(10)

    driver.quit()

if __name__ == "__main__":
    send()