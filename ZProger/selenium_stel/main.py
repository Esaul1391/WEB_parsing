from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
chrome_path='/usr/local/bin/google-chrome'
# options.add_argument("--headless")

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


for page in range(1, 4):
        domain = "https://www.russiadiscovery.ru/"
        url = f"https://www.russiadiscovery.ru/tours/trekkingi/page/{page}/"
        driver.get(url) # перехожу на указанную страницу
        # blocks = driver.find_element(By.CLASS_NAME, "d-catalog__cards-group")
        # posts = blocks.find_elements(By.TAG_NAME, "d-catalog__card")
        # for post in posts:
        #     title = post.find_element(By.CLASS_NAME, 'd-catalog__card-image d-catalog__card-image_shadow').find_element(By.TAG_NAME, "a").get_attribute('href')
        #     print(title)




driver.get(url)
time.sleep(5)
driver.quit()