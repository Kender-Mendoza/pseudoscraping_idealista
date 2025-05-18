import httpx
from ipdb import set_trace as pry


class Idealista:
    BASE_URL = "https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/alquiler/cataluna/barcelona-provincia/barcelona/"

    def __init__(self) -> None:
        pass

    def getData(self) -> httpx.Response:
        proxy = "https://179.60.53.28:80"

        headers = {
            "User-Agent": "Chrome/122.0.0.0 Safari/537.36"
            # (
            #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            #     "AppleWebKit/537.36 (KHTML, like Gecko) "

            # ),
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            # "Accept-Language": "en-US,en;q=0.5",
            # "Connection": "keep-alive",
        }

        with httpx.Client(proxy=proxy, headers=headers, timeout=10) as client:
            try:
                response = client.get(self.BASE_URL, headers=headers)
                print(response)
                response.raise_for_status()

                return response.json()
            except httpx.HTTPStatusError as e:
                raise RuntimeError(f"Error: {e}")
            except httpx.RequestError as e:
                raise RuntimeError(f"{e}")


Idealista().getData()

# ["ciutat-vella", "eixample", "gracia", "sants-montjuic", "sant-marti"]
