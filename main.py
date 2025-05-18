from pyauto import Pyauto
import pandas as pd


def main():
    BASE_URL = "https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/alquiler/cataluna/barcelona-provincia/barcelona"
    pa = Pyauto()

    pa.open_browser(browser="brave")

    for item in ["ciutat-vella", "eixample", "gracia", "sants-montjuic", "sant-marti"]:
        # Get Evolution #
        pa.open_new_browser_tab()
        pa.write_in_browser_url(f"{BASE_URL}/{item}")

        pa.open_browser_console()
        pa.write_script(1)
        jsonData = pa.get_daily_activities_json()

        df = pd.DataFrame(jsonData)
        df.to_csv(
            f"csv_data/Evolución del precio de la vivienda en alquiler en {item}.csv",
            index=False,
            encoding="utf-8",
        )

        pa.close_unnecessary_tab()
        pa.close_unnecessary_tab()

        # Get history #
        pa.open_new_browser_tab()
        pa.write_in_browser_url(f"{BASE_URL}/{item}/historico")

        pa.open_browser_console()
        pa.write_script(0)
        jsonData = pa.get_daily_activities_json()

        df = pd.DataFrame(jsonData)
        df.to_csv(
            f"csv_data/Histórico de precios de alquiler en {item}.csv",
            index=False,
            encoding="utf-8",
        )

        pa.close_unnecessary_tab()
        pa.close_unnecessary_tab()


if __name__ == "__main__":
    main()
