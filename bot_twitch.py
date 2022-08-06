import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

#AAAAA-AAAAA-AAAAA-AAAAA

#link = input("Link: ") #https://www.twitch.tv/mrnoino
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe", chrome_options = chrome_options)

os.system('cls' if os.name == 'nt' else 'clear')

driver.get("https://www.epicgames.com/store/pt-BR/login")
window_before = driver.window_handles[0]

time.sleep(1)

element = driver.find_element_by_xpath('//*[@id="login-with-google"]')
element.click()

time.sleep(1)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

element = driver.find_element_by_xpath('//*[@id="identifierId"]')
element.send_keys("nuno.miguelsl25")

element = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
element.click()

time.sleep(1)

element = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
element.send_keys(input("Password email: "))

element = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
element.click()

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

driver.switch_to.window(window_before)

driver.get("https://www.epicgames.com/store/pt-BR/redeem")

driver.execute_script("window.open('');")

time.sleep(0.5)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

driver.get("https://www.twitch.tv/mrnoino")

element = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button')
element.click()

time.sleep(0.5)

element = driver.find_element_by_xpath('//*[@id="login-username"]')
element.send_keys("MrNoino")

pwd = input("Password twitch: ")
element = driver.find_element_by_xpath('//*[@id="password-input"]')
element.send_keys(pwd)

element = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button')
element.click()

os.system('cls' if os.name == 'nt' else 'clear')

option = input("\tMenu\n1 - Procurar\n0 - Sair\nOpção: ")
print("\n")

erro = 0
while (int(option) != 0):

    os.system('cls' if os.name == 'nt' else 'clear')

    class_name = "text-fragment"

    element = driver.find_elements_by_class_name(class_name)

    i = len(element)-1

    x = 3

    while i>=0 and x>0:

        if(re.search("[A-Z0-9]{5}[-]{1}[A-Z0-9]{5}[-]{1}[A-Z0-9]{5}[-]{1}[A-Z0-9]{5}",element[i].text)):
            print("!!!\tFound\t!!!\n")
            break


        i-=1
        x-=1

    if(i<0 or x==0):
        erro += 1
        print(str(erro) + " - Não encontrou, vou tentar novamente!\n")
        time.sleep(0.5)
        option = 1
    else:
        option = input("\tMenu\n1 - Procurar\n0 - Sair\nOpção: ")
        print("\n")

driver.close()
os.system('cls' if os.name == 'nt' else 'clear')