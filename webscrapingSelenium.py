from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website = "https://coinmarketcap.com/gainers-losers/"
path = "C:/Users/Richard/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
# //*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[1]
container = driver.find_elements(By.XPATH, '//tr[contains(@style, "cursor:pointer")]')

n = 0

names = []
prices = []
changes = []
volumes = []

for container in container:
    n = n + 1
    # //*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[2]/a/div/div/div/p
    name = container.find_element(By.XPATH, './td[2]/a/div/div/div/p').text
    # //*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]/span
    price = container.find_element(By.XPATH, './td[3]/span').text
    # //*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[4]/span
    change = container.find_element(By.XPATH, './td[4]/span').text
    # //*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[5]
    volume = container.find_element(By.XPATH, './td').text
    # print(f'Rank: {n} | Name: {name.text}, Price: {price.text}, Change: {change.text}, Volume: {volume.text}')
    names.append(name)
    prices.append(price)
    changes.append(change)
    volumes.append(volume)

wtf = pd.DataFrame({'Name': names, 'Price': prices, 'Change': changes, 'Volume': volumes})

print(wtf)

wtf.to_csv('coins.csv')
driver.quit()
