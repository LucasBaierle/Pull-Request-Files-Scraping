from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait

config = {
    'EMAIL': '',
    'PASSWORD': '',
    'URL': 'https://github.com/login',
    'PRFiles': 'https://github.com/NOME_REPOSITORIO/pull/NUMERO_DA_PR/files',
    'SleepTime': 10 #Tempo de Carregando da página, quando maior a PR mais segundos precisa
}

def main():
    driver = webdriver.Chrome('./chromedriver')

    driver.get(config['URL'])

    username = driver.find_element_by_xpath('//*[@id="login_field"]')
    username.send_keys(config['EMAIL'])
  
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(config['PASSWORD'])
  
    sigin = driver.find_element_by_css_selector("input[name='commit'][type='submit']")
    sigin.click()

    driver.get(config['PRFiles'])

    time.sleep(config['SleepTime'])

    index = 'Link--primary Truncate-text'

    html =  driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    fileTree = soup.find_all(class_= index)

    f=open('fileTree' + ".txt","w")

    for i in fileTree: 
        f.write('\n' + str(i.text))

    f.close()

    print('fim')

if __name__ == '__main__':
    main()