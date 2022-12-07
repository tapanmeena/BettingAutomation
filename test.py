from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("mary.jewelry")
# browser.find_element_by_id("nav-search").send_keys("Selenium")

print (browser)
# browser.quit()