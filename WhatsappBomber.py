from selenium import webdriver
import os

os.system("clear")

print("\033[1;32;40m ░░░░░██╗░█████╗░██╗░░██╗███████╗██████╗░  ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░")
print("\033[1;32;40m ░░░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗  ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
print("\033[1;32;40m ░░░░░██║██║░░██║█████═╝░█████╗░░██████╔╝  ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝")
print("\033[1;32;40m ██╗░░██║██║░░██║██╔═██╗░██╔══╝░░██╔══██╗  ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
print("\033[1;32;40m ╚█████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║")
print("\033[1;32;40m ░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝\n")
print("                            This Script Was Made By JOKER HACKER​​​​​                          ")

driver = webdriver.Firefox('geckodriver')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('hnQHL')
    button.click()