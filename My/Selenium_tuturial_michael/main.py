from selenium import webdriver
from selenium.webdriver.common.by import By

driwer = webdriver.Chrome()
driwer.get('https://www.thingiverse.com/')
element = driwer.find_elements(By.CSS_SELECTOR, 'class="ThingCardHeader__cardTitleLink--VWcmp"')
print(element)