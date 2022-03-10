from selenium import webdriver
from time import sleep
import json

navegador = webdriver.Firefox()
url = 'https://www.globo.com/'
meu_dicionario = {}


navegador.get(url)
sleep(1)
link = '/noticias'

ancoras = navegador.find_elements_by_class_name('post__link')
for a in ancoras:
    if link in a.get_attribute('href'):
        meu_dicionario.update({a.get_attribute("href"): a.text})


meu_json = json.dumps(meu_dicionario)

with open('news.json', 'w') as file:
        file.write(meu_json)



navegador.quit()
