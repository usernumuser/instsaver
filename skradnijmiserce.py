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


def get_post_path():
    pass

def get_first_post():
    driver.get("https://www.instagram.com/official_kacler2003")
    time.sleep(5)
    #tu się będzie odbywała magia i czary i wgl ten kurwa no przeczttaj co tu się dzieje po prostu XDD
    driver.find_element(By.CSS_SELECTOR, 'div[class="_aabd _aa8k _aanf"]').click()
    time.sleep(5)
    #div[class="_aagu"]
    do_opierdolenia = BeautifulSoup(driver.find_element(By.CSS_SELECTOR, 'ul[class="_acay"]').get_attribute('innerHTML'), 'html.parser').find("img")["src"]
    """
    print(do_opierdolenia)
    lol = open("cipeczka.txt", "w", encoding="utf-8")
    lol.write(do_opierdolenia)
    """
    time.sleep(3)
    driver.get(do_opierdolenia)
    time.sleep(3)
    driver.save_screenshot("screenshot.png")



init()
get_first_post()

while True:
    pass




"""
kod guzika który przełącza mioędzy postami
<button class="_abl-" type="button"><div class="_abm0"><span style="display: inline-block; transform: rotate(90deg);"><svg aria-label="Dalej" class="_ab6-" color="#000000" fill="#000000" height="16" role="img" viewBox="0 0 24 24" width="16"><path d="M21 17.502a.997.997 0 01-.707-.293L12 8.913l-8.293 8.296a1 1 0 11-1.414-1.414l9-9.004a1.03 1.03 0 011.414 0l9 9.004A1 1 0 0121 17.502z"></path></svg></span></div></button>

"""