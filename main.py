import os
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

URL = "https://form.waitlistpanda.com/go/vVGRjdIyHpU1eOCI83x6?ref=de0ORQmV7S35fFymfC7U"
start_time = time.time()


with open("mails.txt") as file:
    mails = file.readlines()
    mails = [x.strip() for x in mails]

with open("twitters.txt") as file:
    twitters = file.readlines()
    twitters = [x.strip() for x in twitters]

with open("wallets.txt") as file:
    wallets = file.readlines()
    wallets = [x.strip() for x in wallets]

addresses = []

for wallet in wallets:
    tmp = wallet.split(" ")[0]
    addresses.append(tmp)

for i in range(5):
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en-US")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    print(f"[{i}] Перехожу на сайт")

    browser.get(
        URL,
    )

    sleep(1)

    inputs = browser.find_elements(By.XPATH, "//input")

    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(mails[i])
    inputs[2].send_keys(twitters[i])

    buttons = browser.find_elements(By.XPATH, "//button")
    buttons[1].click()
    sleep(2)

    with open("ready.txt", "a+") as file:
        file.write(f"{addresses[i]} {mails[i]} {twitters[i]} \n")

    print(f"[{i + 1}] Зарегистрирован")

    browser.quit()

print("--- %s seconds ---" % (time.time() - start_time))
