import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from typing import Annotated, Optional
from typing_extensions import TypedDict

with open('./api_key/API_KEY.txt', 'r') as api:
    os.environ["OPENAI_API_KEY"] = api.read()

def click_close(driver: webdriver.Chrome):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'flex') and contains(@class, 'justify-between') and contains(@class, 'p-3')]//button")
        )
    )
    button.click()
    
def click_buy(driver: webdriver.Chrome):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[2]/div[6]/button[3]")
        )
    )
    button_final_buy = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div/div[3]/div/div[3]/div/button[2]")
        )
    )
    button.click()
    time.sleep(0.5)
    button_final_buy.click()
    
def click_buy(driver: webdriver.Chrome):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/div[2]/div/div[4]/div/input")
        )
    )
    button_final_buy = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div/div[3]/div/div[3]/div/button[2]")
        )
    )
    button.click()
    time.sleep(0.5)
    button_final_buy.click()
    
def x2bee_login(driver: webdriver.Chrome, id:str="x2bee", pw:str="admin"):
    driver.get("https://fo-dev.x2bee.com/login?moveURL=")
    login_id_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div/form/div[1]/input")
        )
    )
    login_pw_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div/form/div[2]/input")
        )
    )
    login_id_input.click()
    login_id_input.send_keys(id)
    login_pw_input.click()
    login_pw_input.send_keys(pw)
    time.sleep(0.5)
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div/form/button")
        )
    )
    login_button.click()
    time.sleep(1.5)

def search_item(driver: webdriver.Chrome, text:str = None):
    search_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/header/div[1]/div[2]/div[2]/div/div[1]/input")
        )
    )
    
    search_div.click()
    search_div.send_keys(text)
    search_div.send_keys(Keys.RETURN)
    
def search_product_list(driver: webdriver.Chrome):
    product_div = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div/div/div/div[3]/div[2]/div[4]/div[1]/ul")
        )
    )
    product_elements = product_div.find_elements(By.TAG_NAME, "li")
    product_info = []
    for product in product_elements:
        try:
            product_name = product.find_element(
                By.XPATH, "./a/div/div[2]/div[1]/p[2]"
            ).text
            product_price = product.find_element(
                By.XPATH, "./a/div/div[2]/div[2]/span"
            ).text
            product_url = product.find_element(
                By.XPATH, "./a"
            ).get_attribute("href")
            
            product_name = product_name.rsplit("(", 1)[0].strip()
            product_price = float(product_price.replace(",", "").replace("원", ""))
            product_info.append((product_name, product_price, product_url))
        except Exception as e:
            print(f"Error fetching product name: {e}")
    
    return product_info