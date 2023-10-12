import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")  # Если вы хотите скрытое (без GUI) выполнение
driver = webdriver.Chrome()



url = 'https://www.vseinstrumenti.ru/category/bolgarki-ushm-123/'
driver.get(url)


page_source = driver.page_source
