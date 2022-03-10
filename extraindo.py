from selenium import webdriver
from time import sleep
import json

navegador = webdriver.Firefox()
url = 'https://lapadalapada.com.br/'
meu_dicionario = {}


navegador.get(url)
sleep(1)
link = '2022/01'

ancoras = navegador.find_elements_by_tag_name('a')

for elemento in ancoras:
    if link in elemento.get_attribute('href'):
        meu_dicionario.update({elemento.get_attribute("href"): elemento.text})


meu_json = json.dumps(meu_dicionario)

with open('news.json', 'w') as file:
        file.write(meu_json)



navegador.quit()
