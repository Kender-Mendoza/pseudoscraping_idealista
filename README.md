# PseudoScraper con PyAutoGUI

Este proyecto es un script de **pseudo-scraping** que utiliza `PyAutoGUI` para extraer información visualmente desde una página web, simulando la interacción de un usuario humano.

## 🧠 ¿Por qué "pseudo"-scraping?

Porque **no utiliza técnicas tradicionales** de scraping como peticiones HTTP, `BeautifulSoup`, `Selenium` o `Playwright`, sino que automatiza el uso del navegador a través del mouse y teclado usando `PyAutoGUI`. Esto permite sortear validaciones automáticas anti-bots sin necesidad de gestionar headers, captchas o sesiones.

---

## ✅ Ventajas

- **Evita bloqueos de bots**: No es necesario gestionar cookies, headers, proxys o captchas.
- **Rápido de implementar** si ya sabes qué y dónde extraer.
- **No requiere análisis del DOM ni de red.**

---

## ❌ Desventajas

- **Bloquea la PC durante su ejecución**, ya que mueve el mouse y escribe en tiempo real.
- **No es robusto**: pequeños cambios en la interfaz pueden romper el flujo.
- **No es reutilizable directamente**: es muy específico al flujo y resolución de pantalla del creador.

---

## 🚨 NOTA
En la carpeta other_options encontrarás pruebas realizadas con:

	•	Playwright
	•	Selenium
	•	httpx

Estos métodos funcionaban parcialmente, pero debido a las validaciones y bloqueos de la web objetivo, se optó finalmente por PyAutoGUI.

## 📦 Instalación

Asegúrate de tener Python instalado (recomendado 3.8+). Luego, instala las dependencias necesarias:

```
pip install -r requirements.txt
```

## 🚀 Ejecución

Una vez instaladas las dependencias, ejecuta el script principal:

```
python -m main.py
```

Asegúrate de no mover el mouse ni interactuar con el teclado mientras el script se ejecuta, ya que PyAutoGUI simula estas acciones y puede interrumpirse fácilmente.