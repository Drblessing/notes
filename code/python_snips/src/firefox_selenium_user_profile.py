# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

profile_path = (
    "/Users/dbless/Library/Application Support/Firefox/Profiles/vho7yigg.selenium"
)

options = Options()
options.add_argument("-profile")
options.add_argument(profile_path)


driver = webdriver.Firefox(options=options)

driver.get("https://www.linkedin.com")

time.sleep(4)

driver.quit()
