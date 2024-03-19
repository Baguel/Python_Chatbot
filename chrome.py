from selenium import webdriver
import time

def web(site):
    driver = webdriver.Chrome()
    url = "https://" + site + ".com" + "/"
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(url)
    print(input("Appuyez sur Entrer pour fermer la fenetre......"))
    driver.quit()