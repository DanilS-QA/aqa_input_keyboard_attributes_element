from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

# Поле Full Name
input_full_name = driver.find_element("xpath", "//input[@id='userName']")
input_full_name.clear()  # Очистка поля
assert input_full_name.get_attribute("value") == ""  # Проверка очистки
input_full_name.send_keys("Ivan")  # Ввод значения
assert "Ivan" in input_full_name.get_attribute("value")  # Проверка ввода

# Поле Email
input_email = driver.find_element("xpath", "//input[@id='userEmail']")
input_email.clear()  # Очистка поля
assert input_email.get_attribute("value") == ""  # Проверка очистки
input_email.send_keys("test@mail.com")  # Ввод значения
assert "test@mail.com" in input_email.get_attribute("value")  # Проверка ввода

# Текстовая область Current Address
textarea_current_address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
textarea_current_address.clear()  # Очистка поля
assert textarea_current_address.get_attribute("value") == ""  # Проверка очистки
textarea_current_address.send_keys("г. Москва, ул. Победы, д. 10, кв. 5")  # Ввод значения
assert "г. Москва, ул. Победы, д. 10, кв. 5" in textarea_current_address.get_attribute("value")  # Проверка ввода

# Текстовая область Permanent Address
textarea_permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
textarea_permanent_address.clear()  # Очистка поля
assert textarea_permanent_address.get_attribute("value") == ""  # Проверка очистки
textarea_permanent_address.send_keys("г. Москва, ул. Победы, д. 10, кв. 5")  # Ввод значения
assert "г. Москва, ул. Победы, д. 10, кв. 5" in textarea_permanent_address.get_attribute("value")  # Проверка ввода

# Закрытие браузера
driver.quit()
