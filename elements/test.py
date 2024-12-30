from driver_tool import *
from x2bee_driver import *

# url = "https://www.danawa.com/"
url = "https://shopping.naver.com/ns/home"
# url = "https://fo-dev.x2bee.com/"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get(url)

# click_close(driver=driver)
# x2bee_login(driver=driver)
# search_item(driver=driver, text="겨울 산행")
# search_product_list(driver=driver)


input_element_list = html_element_search(driver, serach_element="input", by="tag", output="str")
input_item = gpt_element_finder(input_element_list, serach_element="search box input")
query_entry_tool(driver, input_item, "노트북")
time.sleep(10)
item_element_list = html_element_search(driver, serach_element="item", by="class", output="list")

result = gpt_element_finder(item_element_list, serach_element="item")
time.sleep(10)

driver.quit()