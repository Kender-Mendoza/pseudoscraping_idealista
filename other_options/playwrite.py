from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        # Inicia el navegador en modo visible y con bandera antidetec
        browser = p.chromium.launch(
            headless=False, args=["--disable-blink-features=AutomationControlled"]
        )

        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0.0.0 Safari/537.36"
            ),
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://google.com",
            },
        )

        page = context.new_page()

        # Ir a una web de prueba para verificar cabeceras
        # page.goto("https://httpbin.org/headers")
        page.goto("https://www.idealista.com")
        page.wait_for_timeout(100000)  # Espera 1 segundo como humano

        print(page.text_content("body"))

        # Puedes hacer scraping aquí o interactuar con la web
        # page.goto("https://tuwebobjetivo.com")

        browser.close()


if __name__ == "__main__":
    main()
