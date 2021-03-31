from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import alert_is_present
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(
    executable_path="Your Driver Path", chrome_options=chrome_options)
driver.get("https://www.fb.com")
driver.find_element_by_id("email").send_keys("Your Email Address")
driver.find_element_by_id("pass").send_keys("Your Password")
driver.find_element_by_id("u_0_b").click()
driver.implicitly_wait()
print("Completed")
