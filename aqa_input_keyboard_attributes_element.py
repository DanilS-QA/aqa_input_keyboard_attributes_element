from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

Input_Full_Name = driver.find_element("xpath", "//input[@id='userName']")
Input_Full_Name.clear()
assert Input_Full_Name.get_attribute("value") == ""
Input_Full_Name.send_keys("Ivan")
assert "Ivan" in Input_Full_Name.get_attribute("value")

Input_Email = driver.find_element("xpath", "//input[@id='userEmail']")
Input_Email.clear()
assert Input_Email.get_attribute("value") == ""
Input_Email.send_keys("test@mail.com")
assert "test@mail.com" in Input_Email.get_attribute("value")

Textarea_Current_Address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
Textarea_Current_Address.clear()
assert Textarea_Current_Address.get_attribute("value") == ""
Textarea_Current_Address.send_keys("г. Москва, ул. Победы, д. 10, кв. 5")
assert "г. Москва, ул. Победы, д. 10, кв. 5" in Textarea_Current_Address.get_attribute("value")

Textarea_Permanent_Address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
Textarea_Permanent_Address.clear()
assert Textarea_Permanent_Address.get_attribute("value") == ""
Textarea_Permanent_Address.send_keys("г. Москва, ул. Победы, д. 10, кв. 5")
assert "г. Москва, ул. Победы, д. 10, кв. 5" in Textarea_Permanent_Address.get_attribute("value")