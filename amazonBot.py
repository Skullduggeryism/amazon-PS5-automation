import os
import time
from os.path import join, dirname
from logger import logger as l
from selenium.common.exceptions import *
from dotenv import load_dotenv
from amazoncaptcha import AmazonCaptcha

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LOGIN_MAIL = os.environ.get('LOGIN_MAIL', None)
LOGIN_PASSWORD = os.environ.get('LOGIN_PASSWORD', None)

ITEM_URL = os.environ.get('ITEM_URL', None)

ACCEPT_SHOP = 'Amazon.com'
#LIMIT_VALUE = 500    # Maximum USD for the purchase
LIMIT_VALUE = os.environ.get('LIMIT_VALUE', None) # Let's add this to the .env file



def login(chromeDriver):
    chromeDriver.find_element_by_id("nav-link-accountList").click()
    chromeDriver.find_element_by_id('ap_email').send_keys(LOGIN_MAIL)
    chromeDriver.find_element_by_id('continue').click()
    chromeDriver.find_element_by_id('ap_password').send_keys(LOGIN_PASSWORD)
    chromeDriver.find_element_by_id('signInSubmit').click()
    l.info("Successfully logged in")

def validate_captcha(chromeDriver):
    time.sleep(1)
    l.info("Solving CAPTCHA")
    chromeDriver.get('https://www.amazon.com/errors/validateCaptcha')
    captcha = AmazonCaptcha.fromdriver(chromeDriver)
    solution = captcha.solve()
    chromeDriver.find_element_by_id('captchacharacters').send_keys(solution)
    chromeDriver.find_element_by_class_name('a-button-text').click()
    time.sleep(1)

def purchase_item(chromeDriver):
    chromeDriver.get(ITEM_URL)
    l.info("Checking stock")
    if not in_stock_check(chromeDriver): 
        return False
    # Checks price
    l.info("Checking price")
    if not verify_price_within_limit(chromeDriver):
        return False
    # Checks seller
    l.info("Checking seller")
    if not seller_check(chromeDriver):
        return False
    l.info("Clicking buy now")
    chromeDriver.find_element_by_id('buy-now-button').click()
    # clickbuynow = chromeDriver.find_element_by_id('buy-now-button')
    # while clickbuynow.is_displayed():
    #     clickbuynow.click() # 1 click buy
    #     chromeDriver.refresh()
    #     time.sleep(10)
    #     clickbuynow = chromeDriver.find_element_by_id('buy-now-button')
      
    l.info("Placing order")
    chromeDriver.find_element_by_name('placeYourOrder1').click()
    # while true:        
    #     try:
    #         chromeDriver.find_element_by_name('placeYourOrder1').click()
    #     except NoSuchElementException:
    #         break
    l.info("Successfully purchased item")
    os._exit(0)

def in_stock_check(chromeDriver):
    inStock = False
    try:
        stock = chromeDriver.find_element_by_id('availability').text
        availability = stock.find("In Stock")
        if availability == -1:
            l.info("Item is not in stock")
            raise Exception("Item is not in stock")
            return False
        elif availability == 0:
            l.info("Item is in stock!")
            inStock = True
    finally:
        return inStock

def seller_check(chromeDriver):
    element = chromeDriver.find_element_by_id('tabular-buybox-truncate-1').text
    l.info('Seller: {}'.format(element))
    shop = element.find(ACCEPT_SHOP)
    if shop == -1:
        raise Exception("Amazon is not the seller")
        return False
    l.info("Successfully verified Seller")
    return True

def verify_price_within_limit(chromeDriver):
    price = chromeDriver.find_element_by_id('priceblock_ourprice').text
    price = price.replace('$', '')
    price = float(price)
    l.info('price of item is:  {}'.format(price))
    l.info('limit value is: {}'.format(float(LIMIT_VALUE)))
    # int_price = int(price.replace(' ', '').replace(',', '').replace('$', ''))
    if price > float(LIMIT_VALUE):
        l.warn('PRICE IS TOO LARGE.')
        return False
    return True
