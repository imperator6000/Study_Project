from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
import time

#PATH = "C:/UsersI355372/Documents/Duc/Personal-Project/Study_Project/Crawl_Aliproduct_APi/chromedriver.exe"
option = Options()     
# option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")
# option.add_experimental_option("prefs", { 
#     "profile.default_content_setting_values.notifications": 2 
# })
driver = webdriver.Firefox()
driver.get("https://aliexpress.com")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# cookies = pickle.load(open("cookies.pickle", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)


def extract_product_urls_from_list_page(list_page_url):
    driver.get(list_page_url)
    time.sleep(5)
    cats = driver.find_elements_by_css_selector('span.title')

    all_links = set()
    for ind, cat in enumerate(cats):
        print(cat.text)
        try:
            cat.click()
        except Exception:
            continue
        if ind == 0:
            items = driver.find_elements_by_class_name('item-desc')
            links = [item.get_attribute('href') for item in items]
        else:
            items = driver.find_elements_by_css_selector('div.title > a')
            links = [item.get_attribute('href') for item in items]
        for link in links:
            all_links.add(link)
        time.sleep(2)
    return all_links


if __name__ == '__main__':
    extract_product_urls_from_list_page('https://sale.aliexpress.com/__pc/bestselling.htm')