from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import tkinter as tk

from time import sleep

import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='registro_pesquisas'
)

cursor = connection.cursor()

window = tk.Tk()

window.geometry('400x400')


def Start():

    entry = music_search.get()

    if not entry:
        print('erro: campo de pesquisa vazio')
    else:
        print(entry)

        cursor.execute(f'INSERT INTO history (search) VALUES ("{entry}")')

        connection.commit()

        driver = webdriver.Chrome()

        driver.get('https://music.youtube.com/')

        pesquisa = driver.find_element(By.XPATH, "//input[@id='input']")

        pesquisa.click()

        sleep(1)

        


        pesquisa.send_keys(entry) # subtituir por uma entrada

        pesquisa.send_keys(Keys.ENTER)

        sleep(4)

        video = driver.find_elements(By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--enable-backdrop-filter-experiment']")

        video[0].click()
        
start_button = tk.Button(
    window,
    text='Iniciar Programa',
    width=15,
    command=Start
)

music_search = tk.Entry(
    window,
    width=15
)

label = tk.Label(
    window,
    text='clique aqui e espere a mágica acontecer'
)

start_button.place(
    relx=0.5,
    rely=0.5,
    anchor='c'
)

label.place(
    relx=0.5,
    rely=0.3,
    anchor='c'
)

music_search.place(
    relx=0.5,
    rely=0.4,
    anchor='c'
)

window.mainloop()
