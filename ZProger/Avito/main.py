from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

#options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://www.avito.ru/moskva/bytovaya_elektronika?cd=1&q=3d+принтер"
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.quit()