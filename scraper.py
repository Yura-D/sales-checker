import time
from selenium import webdriver

# tests data
PATH = '/html/body/div[2]/main/div[2]/div/div[1]/div[3]/form/div/div/div/div/div[1]/div[1]/div[1]/div[1]/span'
URL = 'https://eva.ua/ua/pr12515/'


def convert_price(text):
    price = text.split()[0]
    price = price.replace(',', '.')
    return float(price)


def get_price(url, path):
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get(url)
    # TODO Change sleep func
    time.sleep(1)
    element = driver.find_element_by_xpath(path)
    return convert_price(element.text)


if __name__ == '__main__':
    print(get_price(URL, PATH))
