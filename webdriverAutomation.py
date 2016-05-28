
from selenium import webdriver

#driver=webdriver.Firefox()
driver=webdriver.Chrome()
driver.set_page_load_timeout(30)
driver.get("http://www.google.com")
#driver.maximize_window()
driver.get_screenshot_as_file("snapshot.png")
driver.quit()
