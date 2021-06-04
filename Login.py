# Requirements:
# pip install selenium
# pip install undetected_chromedriver

username = 'your@email.com'
password = 'yourpassword'
from time import sleep
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver.v2 as uc

driver = uc.Chrome()
try:
    driver.get('https://accounts.google.com/signin')
    sleep(2)
    driver.find_element_by_id("identifierId").send_keys(username, Keys.ENTER)
    sleep(2)
    driver.find_element_by_xpath("//input[contains(@name,'password')]").send_keys(password, Keys.ENTER)
    input(">>>Press Enter to shutdown...")
except Exception as e:
    print(e)
