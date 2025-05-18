import json
import pyperclip
from log_method import log_method
import pyautogui
import time


class Pyauto:
    @log_method
    def open_browser(self, browser):
        pyautogui.keyDown("command")
        pyautogui.press("space")
        time.sleep(2)
        pyautogui.keyUp("command")
        pyautogui.typewrite(browser)
        pyautogui.press("enter")
        time.sleep(2)

    @log_method
    def open_new_browser_tab(self):
        pyautogui.keyDown("command")
        pyautogui.press("t")
        time.sleep(2)
        pyautogui.keyUp("command")

    @log_method
    def write_in_browser_url(self, url):
        pyautogui.typewrite(url)
        pyautogui.press("enter")
        time.sleep(2)

    @log_method
    def close_unnecessary_tab(self):
        pyautogui.keyDown("command")
        pyautogui.press("w")
        time.sleep(2)
        pyautogui.keyUp("command")

    @log_method
    def open_browser_console(self):
        pyautogui.keyDown("command")
        pyautogui.keyDown("option")
        pyautogui.press("j")  # this is for brave
        time.sleep(2)
        pyautogui.keyUp("command")
        pyautogui.keyUp("option")

        # waiting for console warnings
        time.sleep(1)

    @log_method
    def write_script(self, table_index):
        pyautogui.typewrite(
            f"const table = document.querySelectorAll('table')[{table_index}]"
        )
        pyautogui.press("enter")

        content = ""
        with open("table_to_json.min.js", "r", encoding="utf-8") as file:
            content = file.read()

        pyautogui.typewrite(content)
        time.sleep(10)
        pyautogui.press("enter")

    @log_method
    def get_daily_activities_json(self):
        pyautogui.keyDown("command")
        pyautogui.press("a")
        time.sleep(1)
        pyautogui.press("c")
        time.sleep(2)
        pyautogui.keyUp("command")

        json_string = pyperclip.paste()
        return json.loads(json_string)
