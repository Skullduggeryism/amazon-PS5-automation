# Amazon Purchase Script 

**Use at your own risk. Read thoroughly**

Example: script to buy items on Amazon (Please do not use this script for scalping, this is simply a free open source solution for those that want a console but are unable to get one due to market competitiveness)


forked from yosh1/amazon-automation & druyang/amazon-PS5-automation

Updates: 
--- 
  * Solves for CAPTCHA

Requirements: 
--- 
* Python 3 
* Python modules in `requirements.txt` 
* [WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) in same directory 

Recommended to be run on Linux or Max. Would be a good script to run on a raspberry pi or server

To do:
--- 
  * Make the Buy Now click and the Place Order click loop until they're successful - difficult to test
  * Solve CAPTCHA's less frequently, or only when required

Notes of caution: 
--- 

Things to check for on Amazon/potential edge cases: 

 * Currently Amazon 2FA needs to be disabled on your account (this will **expose your account to security problems**)
 * Currently uses 1 click buy. Confirm your default address + payments is correct before running this script
 

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

