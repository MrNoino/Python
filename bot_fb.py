from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
driver.get("https://pt-pt.facebook.com")
field = driver.find_element_by_css_selector("#email")
f1 = input("Email ou numero de telefone: ")
field.send_keys(f1)
field = driver.find_element_by_css_selector("#pass")
f2 = input("Password: ")
field.send_keys(f2)
field = driver.find_element_by_css_selector("#u_0_d")
field.click()
