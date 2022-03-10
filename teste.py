from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from time import sleep

navegador = webdriver.Firefox()
url = 'https://www.facebook.com/'
navegador.get(url)
navegador.implicitly_wait(2)
sleep(2)
"""
Abrindo o json 'news.json' para voltar em forma de dicionario
pegando as chaves e os valores do dicionario para colocarr no campo(post_box)
"""

with open('news.json', 'r') as file:
    noticias_json = file.read()
    noticias_dic = json.loads(noticias_json)


def fazendo_login(navegador, gmail, senha):
    username = navegador.find_element_by_name('email')
    username.send_keys(gmail)

    password = navegador.find_element_by_name('pass')
    password.send_keys(senha)

    enter = navegador.find_element_by_name('login')
    enter.click()

def fazendo_post(navegador, noticias):
    for chave in noticias.keys():
            sleep(2)
            divs = navegador.find_element_by_xpath("//div[@class='m9osqain a5q79mjw gy2v8mqq jm1wdb64 k4urcfbm qv66sw1b']")
            divs.click()

            sleep(2)
            post_box = navegador.switch_to.active_element
            post_box.send_keys('Publicado por: globo.com')
            post_box.send_keys(Keys.ENTER)
            post_box.send_keys(noticias_dic[chave])
            post_box.send_keys(Keys.ENTER)
            post_box.send_keys(chave)
            sleep(18)
            post_box.send_keys(Keys.CONTROL + Keys.ENTER)
            sleep(12)
            navegador.refresh();


fazendo_login(navegador, 'matheusggee1314@gmail.com', 'matheus99')
fazendo_post(navegador, noticias_dic)
"""
for chave in noticias_dic.keys():
  #print(chave)
  print(f'A chave é{chave},\n o valor é: {noticias_dic[chave]}')
"""
