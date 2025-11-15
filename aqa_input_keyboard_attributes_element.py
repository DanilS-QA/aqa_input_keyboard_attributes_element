from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

input_full_name = driver.find_element("xpath", "//input[@id='userName']")
input_full_name.clear()
assert input_full_name.get_attribute("value") == ""
input_full_name.send_keys("Ivan")
assert "Ivan" in input_full_name.get_attribute("value")

input_email = driver.find_element("xpath", "//input[@id='userEmail']")
input_email.clear()
assert input_email.get_attribute("value") == ""
input_email.send_keys("test@mail.com")
assert "test@mail.com" in input_email.get_attribute("value")

textarea_current_address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
textarea_current_address.clear()
assert textarea_current_address.get_attribute("value") == ""
textarea_current_address.send_keys("г. Москва, ул. Победы, д. 10, кв. 5")
assert "г. Москва, ул. Победы, д. 10, кв. 5" in textarea_current_address.get_attribute("value")

textarea_permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
textarea_permanent_address.clear()
assert textarea_permanent_address.get_attribute("value") == ""
textarea_permanent_address.send_keys("г. Москва, ул. Победы, д. 10, кв. 5")
assert "г. Москва, ул. Победы, д. 10, кв. 5" in textarea_permanent_address.get_attribute("value")
