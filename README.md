# Amazon Purchase Script 

# Use at your own risk. Read thoroughly
# Use at your own risk.
# Use at your own risk.

This is a Python script that checks if an item is in stock, shipped by Amazon, and under a certain price limit. The script will then purchase the item with limited captcha solving abilities. 

Example: script to buy an item on Amazon (Please do not use this script for scalping, this is simply a free open source solution for those that want a console but are unable to get one)

forked from yosh1/amazon-automation & druyang/amazon-PS5-automation


Notes of caution: 
--- 

Things to check for on Amazon/potential edge cases: 

 * Amazon 2FA (an option is to disable but this will **expose your account to security problems**)
 * 1 Click buy sometimes does not work. Sometimes it does. 
 * **Behavior is dependent on your default shipping address and payment method. Use at your own risk**

Development: 
--- 
## TODO: 
Detect when Amazon sends to captcha by detecting for text on the captcha page. After detecting, call the `validate_captcha` function. 

Requirements: 
--- 
* Python 3 
* Python modules in `requirements.txt` 
* [WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) in same directory 

Recommended to be run on Linux or Max. Would be a good script to run on a raspberry pi or server

--- 

## Logic/Behavior: 
 
 1. Starts Selenium 
 2. Loops the following until all attributes of the item are correct: 
    1. Verifies item is in stock 
    2. Verifies the price is less than the set maximum
    3. Checks to make sure the shipper is from Amazon.com 
        
        *NOTE: I used shipper instead of seller because quite a few items are not actually sold by Amazon.* **Change this on a case by case basis**
4. Logs in 
5. Adds to cart 
6. Checks out  
 

Sample Log: 

    [26/Nov/2020 19:37:36] INFO - Started Chrome
    [26/Nov/2020 19:37:39] INFO - Starting purchase process...
    [26/Nov/2020 19:37:39] INFO - Checking stock...
    [26/Nov/2020 19:37:39] INFO - Item is in-stock!
    [26/Nov/2020 19:37:39] INFO - price of item is:  $39.99
    [26/Nov/2020 19:37:39] INFO - Checking shipper...
    [26/Nov/2020 19:37:39] INFO - Successfully verified shipper as: Amazon
    [26/Nov/2020 19:37:39] INFO - Logging in as username@example.com
    [26/Nov/2020 19:37:41] INFO - Checking out...
    [26/Nov/2020 19:37:57] INFO - Placed order!
    [26/Nov/2020 19:37:57] INFO - Successfully purchased item

Testing notes: 
 * Confirmed loops when item is not in stock 
 * Does not buy when shipper/price are incorrect! 
 * Buys when instock and seller/price are correct 

---

## Copy `.env`

```
$ cp .env.sample .env
```


## Run

```
$ pip install -r requirements.txt 
$ python3 main.py
```

Alternatively use Docker: 

```
$ docker-compose build
$ docker-compose up -d
```

License 
--- 
Under MIT License.
Use at your own risk. 

