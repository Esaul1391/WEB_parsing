import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def get_source_html(url):
    with webdriver.Chrome() as browser:
        # browser.get(url=url)

        # time.sleep(1)
        # height = browser.execute_script("url")
        # print(height)
        # browser.execute_script(f"window.scrollBy(0,{height})")
        # time.sleep(5)
        # find_more_element = browser.find_element(By.ID,"u68754634")
        # actions = ActionChains(browser)
        # actions.move_to_element(find_more_element).perform()
        # time.sleep(3)

        try:
            browser.get(url=url)
            time.sleep(3)
            while True:
                height = browser.execute_script("url")
                browser.execute_script(f"window.scrollBy(0,{height})")
                find_more_element = browser.ind_element(By.TAG_NAME,"show-more-button")
                if browser.find_element("js-next-page button button-show-more button-block button40 button-primary"):
                    with open("lessons/source-page.html", 'w') as file:
                        file.write(browser.page_source)
                    break
                else:
                    action = ActionChains(browser)
                    action.move_to_element(find_more_element).perform()
                    time.sleep(3)

        except Exception as _ex:
            print(_ex)



def get_items_urls(file_path):
    with open(file_path) as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    itms_divs = soup.find_all('div', class_="service_description")

    urls = []
    for item in itms_divs:
        item_url = item.find("div", class_="H3").find("a").get("href")
        urls.append(item_url)

    with open("lesson12/items_urls.txt", 'w') as file:
        for url in urls:
            file.write(f"{url}\n")


    return []

def main():
    get_source_html(url="https://spb.zoon.ru/medical/page-10/")


if __name__ == "__main__":
    main()