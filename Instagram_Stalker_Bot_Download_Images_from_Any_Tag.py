from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import os
import wget     

# Define a ruta ao Chromedriver
chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe') 
service = Service(executable_path=chromedriver_path)


driver = webdriver.Chrome(service=service)
driver.get('http://instagram.com')

# Esperar e aceptar as cookies
try:
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept All') or contains(text(), 'Allow essential and optional cookies')]"))
    )
    cookie_button.click()
except:
    print("No se encontró el botón de cookies o ya fue aceptado.")


username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']" )))

username.send_keys('************')
password.send_keys('xxxxxxxxxxx***xxxx')

entrar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']" )))
entrar.click()


# pop-up "Not Now"
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
except:
    print("Nao se encontrou o botao 'Not Now' o já foi gestionado.")



try:
    # Esperar a que apareça a mensagem da autorizaçao
    consent_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Aceptar') or contains(text(), 'Accept') or contains(text(), 'Revisar')]"))
    )
    consent_button.click()
    print("aceita-se o consentimento para anuncios personalizados.")
except:
    print("Nao se encontrou o botao de consentimento ou já foi gestionado.")

tag='datascientist'
driver.get(f'http://instagram.com/explore/tags/{tag}/')

for j in range(2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

images = driver.find_elements_by_tag_name('img')

len(images)
images = [i.get_attribute('src') for i in images]
images


path = os.path.join(os.getcwd(), tag)
if not os.path.exists(path):
    os.mkdir(path)

for num, image in enumerate(images, start=1):
    save_as = os.path
    wget.download(image, save_as)

# Mantén o navegador aberto por 30 segundos
time.sleep(30)

# Fecha o navegador depois da  pausa
driver.quit()