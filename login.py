import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="D:/Webdrivers/chromedriver_win32/chromedriver.exe", chrome_options = chrome_options)

option = input("\tMenu\n5 - Instagram\n4 - Facebook\n3 - Messenger\n2 - Hotmail\n1 - Gmail\n0 - Sair\nOpção: ")
print("\n")

os.system('cls' if os.name == 'nt' else 'clear')

print("url: " + driver.current_url)

i = 0

urls = [False, False, False, False, False]

while (option != "0"):

    if i != 0 and driver.current_url != "data:," and driver.current_url != "about:blank" and option.isdigit() and urls[int(option)-1] == False:
        driver.execute_script("window.open('');")
        window = driver.window_handles[i]
        driver.switch_to.window(window)

    if option == "1" and urls[0] == False:
        driver.get("https://www.gmail.com/")

        i += 1

        urls[0] = True

    elif option == "2" and urls[1] == False:
        driver.get("https://www.outlook.com/")

        i += 1

        urls[1] = True

    elif option == "3" and urls[2] == False:
        driver.get("https://www.messenger.com/")

        i += 1

        urls[2] = True

    elif option == "4" and urls[3] == False:
        driver.get("https://www.facebook.com/")

        i += 1

        urls[3] = True

    elif option == "5" and urls[4] == False:
        driver.get("https://www.instagram.com/")

        i += 1

        urls[4] = True

    else:
        print("Opção inválida, tente novamente.\n")
    
    print("url: " + driver.current_url)
    option = input("\tMenu\n5 - Instagram\n4 - Facebook\n3 - Messenger\n2 - Hotmail\n1 - Gmail\n0 - Sair\nOpção: ")
    print("\n")

driver.close()
os.system('cls' if os.name == 'nt' else 'clear')