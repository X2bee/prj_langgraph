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

def html_element_search(driver: webdriver.Chrome, serach_element:str = "input", by:str="tag", output="list"):
    if by == "tag":
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, serach_element)))
            all_elements = driver.find_elements(By.TAG_NAME, serach_element)
            input_elements = []
            for element in all_elements:
                if element.tag_name.lower() == serach_element:
                    input_elements.append(element)
        except:
            pass

        input_list = []
        try:
            for input_elem in input_elements:
                input_list.append(input_elem.get_attribute('outerHTML'))
                
            input_list = list(set(input_list))
            input_list = [item for item in input_list if item.strip() != '']
            input_list_text = "\n".join(input_list)
        except:
            pass
        
    elif by == "text":
        try:
            all_elements = driver.find_elements(By.XPATH, "//body//*")
            input_elements = []
            for element in all_elements:
                if serach_element in element.text:
                    input_elements.append(element)
        except:
            pass

        input_list = []
        try:
            for input_elem in input_elements:
                input_list.append(input_elem.text)
                
            input_list = list(set(input_list))
            input_list = [item for item in input_list if item.strip() != '']
            input_list_text = "\n".join(input_list)
        except:
            pass
        
    elif by == "accessible_name":
        try:
            all_elements = driver.find_elements(By.XPATH, "//body//*")
            input_elements = []
            for element in all_elements:
                if serach_element in element.accessible_name:
                    input_elements.append(element)
        except:
            pass

        input_list = []
        try:
            for input_elem in input_elements:
                input_list.append(input_elem.get_attribute('outerHTML'))
                
            input_list = list(set(input_list))
            input_list = [item for item in input_list if item.strip() != '']
            input_list_text = "\n".join(input_list)
        except:
            pass
        
    elif by == "class":
        try:
            all_elements = driver.find_elements(By.XPATH, "//body//*")
            input_elements = []
            for element in all_elements:
                if serach_element:
                    if serach_element in element.get_attribute("class"):
                        input_elements.append(element)
                elif serach_element == None:
                    input_elements.append(element)
        except:
            pass

        input_list = []
        try:
            for input_elem in input_elements:
                input_list.append(input_elem.get_attribute('outerHTML'))
            
            input_list = list(set(input_list))
            input_list = [item for item in input_list if item.strip() != '']
            input_list_text = "\n".join(input_list)
        except:
            pass
        
    if output == "list":
        return input_list
    if output == "str":
        return input_list_text
    
class Find_Searchbar(TypedDict):
    element_id: Annotated[str, ..., "Element's unique id"]
    element_class: Annotated[str, ..., "Element's unique class"]
    element_name: Annotated[str, ..., "Element's unique name"]

model = ChatOpenAI(model="gpt-4o-mini", temperature=0).with_structured_output(Find_Searchbar)

def gpt_element_finder(text, serach_element="input"):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an assistant skilled in analyzing HTML data."),
            ("human", "Analyze the following HTML data and identify the {serach_element} element. Provide its unique identifier (e.g., ID, class, or name).\n\n{html}"),
        ]
    )

    chain = prompt | model
    response = chain.invoke({"serach_element": serach_element, "html": text})
    print(response)
    return response

def query_entry_tool(driver: webdriver.Chrome, input_elements:dict, search_text:str = None):
    input_element = None
    try:
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, input_elements['element_id'])))
    except Exception as e:
        pass

    if not input_element:
        try:
            if input_elements['element_class']:
                input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, input_elements['element_class'].split()[0])))
        except Exception as e:
            pass

    if not input_element:
        try:
            if input_elements['element_name']:
                input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, input_elements['element_name'])))
        except Exception as e:
            pass

    if input_element:
        driver.execute_script("arguments[0].scrollIntoView();", input_element)
        input_element.click()
        input_element.send_keys(search_text)
        input_element.send_keys(Keys.RETURN)
        print("텍스트 입력 성공!")
    else:
        print("Fail to fine search bar.")

