from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()

driver.get('https://music.youtube.com/')

pesquisa = driver.find_element(By.XPATH, "//input[@id='input']")

pesquisa.click()

sleep(1)

pesquisa.send_keys('tribalistar voce é assim um sonho pra mim')

pesquisa.send_keys(Keys.ENTER)

sleep(4)

video = driver.find_elements(By.XPATH, "//ytmusic-responsive-list-item-renderer[@class='style-scope ytmusic-shelf-renderer']//a[contains(@href, 'watch')]")

for i in range(0, len(video)):
    print(video[i].text)

print(f"Número de elementos encontrados: {len(video)}")

video[0].click()

input()