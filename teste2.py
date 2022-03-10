from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from time import sleep


def fazendo_login(navegador, gmail, numero, senha):

    username = navegador.find_element_by_name('text')
    username.send_keys(gmail)

    sleep(2)
    username.send_keys(Keys.TAB)
    username.send_keys(Keys.ENTER)
    sleep(2)
    number = navegador.find_element_by_name('text')
    number.send_keys(numero)

    sleep(2)
    number.send_keys(Keys.TAB)
    number.send_keys(Keys.ENTER)
    sleep(2)

    password = navegador.find_element_by_name('password')
    password.send_keys(senha)
    sleep(2)
    password.send_keys(Keys.TAB)
    password.send_keys(Keys.ENTER)


def fazendo_post(navegador):
    tweet_text_span = navegador.find_element_by_xpath("//div[@data-testid='tweetTextarea_0']/div/div/div/span")

    tweet_text_span.send_keys("Do you know we can tweet with selenium?")

    tweet_button = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']")))
    tweet_button.click()


navegador = webdriver.Firefox()
url = 'https://twitter.com/i/flow/login'
navegador.get(url)

sleep(2)

gmail = 'teste.automatico.2003@gmail.com'
numero = '065996451154'
senha  = 'matheus99AZ'


fazendo_login(navegador, gmail,numero, senha)

fazendo_post(navegador)




#post do tweeter
