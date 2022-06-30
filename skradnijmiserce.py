from selenium import webdriver
from selenium.webdriver.common.by import By
import time, pickle, glob

from bs4 import BeautifulSoup



driver = webdriver.Firefox()



def init():
    if "ciasteczka.cipka" not in glob.glob("*"):
        cipka = input("Username")
        cibga = input("Password")
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "bIiDR").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(cipka)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(cibga)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, 'button[class="sqdOP  L3NKy   y3zKF     "]').click()
        time.sleep(5)
        pickle.dump(driver.get_cookies(), open("ciasteczka.cipka", "wb"))
    else:
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        ciasteczka = pickle.load(open("ciasteczka.cipka", "rb"))
        for cipek in ciasteczka:
            driver.add_cookie(cipek)


def get_posts_data():
    driver.get("https://www.instagram.com/official_kacler2003")
    time.sleep(5)
    #tu się będzie odbywała magia i czary i wgl ten kurwa no przeczttaj co tu się dzieje po prostu XDD
    driver.find_element(By.CSS_SELECTOR, 'div[class="_aabd _aa8k _aanf"]').click()
    time.sleep(5)
    while True:
        #checks if this is a multipost and loads all images/videos
        while True:
            try:
                driver.find_element(By.CSS_SELECTOR, 'button[class=" _aahi"').click()
            except:
                time.sleep(0.5)
                break
        while True:
            try:
                post = BeautifulSoup(driver.find_element(By.CSS_SELECTOR, 'article[role="presentation"]').get_attribute('innerHTML'), 'html.parser')
                zdjecia = post.find_all("img")
                filmy = post.find_all("video")
                if zdjecia or filmy:
                    break
                else:
                    continue
            except:
                time.sleep(0.2)
                continue
            break



        print(filmy)
        lol = open("cipeczka.txt", "w", encoding="utf-8")
        lol.write(str(zdjecia))

        try:
            driver.find_element(By.CSS_SELECTOR, 'div[class=" _aaqg _aaqh"]').click()
        except:
            print("no more posts!")
            break
        time.sleep(2)





init()
get_posts_data()