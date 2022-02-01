from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

from product_display import display_organizer as pd
from price_fixer import fix_price as pf
import time

Chrome_option = Options()
Chrome_option.add_argument("--headless")

Driver_service = Service("./chromedriver")



def get_product_info(links):

    products = []

    for link in links:

        print("\n Getting info...")

        while True:
            try:
                driver = webdriver.Chrome(service= Driver_service, options=Chrome_option)
                driver.get(link)
                break

            except Exception as e:
                print(str(e))
                time.sleep(5)
                continue

        time.sleep(1)

        try:
            name = driver.find_element(By.CLASS_NAME, "page-title")
            price_new = driver.find_elements(By.CLASS_NAME, "product-new-price")
            price_new_sup = price_new[1].find_element(By.TAG_NAME, "sup")

            try:
                price_resealed =  driver.find_element(By.CLASS_NAME, "has-deal")
                price_resealed_sup =  price_resealed.find_element(By.TAG_NAME, "sup")

                description = driver.find_element(By.CLASS_NAME, "panel-resealed-text")

            except NoSuchElementException:
                 price_resealed  = None
                 pass

            

        except Exception as e:
            print(str(e))
            break
        
        if price_resealed:
            full_info = {"type": True, "name": name.text, "new": pf(price_new_sup.text, price_new[1].text), 'resealed': pf(price_resealed_sup.text, price_resealed.text), 'desc': description.text}
            products.append(full_info)
        
        else:
            found_info = full_info = {"type": False, "name": name.text, "new": pf(price_new_sup.text, price_new[1].text)}
            products.append(found_info)
        
        driver.close()

    return pd(products)