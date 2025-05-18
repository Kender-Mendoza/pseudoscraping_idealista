import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import random


def esperar(min_t=2, max_t=4):
    time.sleep(random.uniform(min_t, max_t))


BASE_URL = "https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/alquiler/cataluna/barcelona-provincia/barcelona/"

# Configuración del navegador
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument("--lang=es-ES,es")

# Inicializar navegador
driver = uc.Chrome(options=options)

try:
    # Visita la home para simular entrada humana
    driver.get("https://www.idealista.com/")  # ⚠️ cambia esto por tu URL objetivo
    esperar(3, 6)
    # time.sleep(100000)

    driver.find_element(By.CSS_SELECTOR, "button#didomi-notice-disagree-button").click()
    esperar(2, 4)
    # time.sleep(100000)

    driver.find_element(By.LINK_TEXT, "Sala de prensa").click()
    esperar(2, 4)
    time.sleep(100000)

    # time.sleep(1000)

    # driver.find_element(By.LINK_TEXT, "Informes de precio").click()
    # esperar(4, 6)

    # time.sleep(10000)

    # Ir al objetivo final
    # driver.get("https://example.com/datos")  # ⚠️ cambia esto también
    # esperar(3, 5)

    # Extraer contenido (ejemplo)
    print(driver.page_source)

    # didomi-notice-disagree-button
    # Rechazar

finally:
    driver.quit()
