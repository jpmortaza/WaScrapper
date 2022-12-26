from bs4 import BeautifulSoup
import re
from lxml import etree
import requests

def scrapperWa():
    buscar = input("Enter the search term:")
    x = 0
    while x <= 70:
        url = f'https://www.google.co.ve/search?q=+{buscar}+site:https://chat.whatsapp.com/*&newwindow=1&start={x}&newwindow=1&filter=0&biw=1920&bih=1009&dpr=1'
        HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                    'Accept-Language': 'pt-BR, pt;q=0.5'})
        request_result=requests.get( url, headers=HEADERS)
        soup = BeautifulSoup(request_result.text,"html.parser")
        links_page=soup.find_all( 'h3' )
        x +=10
        print(url)
        for info in links_page:
            link_grupo = info.getText()
            print(link_grupo)
            arquivo = open("content/links.txt", "a")
            grupos = link_grupo
            arquivo.write(f"\n{grupos}")
            

def scrapperGo():
    buscar = input("Enter the search term:")
    site = input("Enter website to extract links: Example: facebook.com")

    x = 0

    while x <= 100:
        url = f'https://www.google.com/search?q=site:{site}+{buscar}+https://chat.whatsapp.com&rlz=1C1FCXM_pt-PTBR997BR997&ei=VOmhY8OoH6_e1sQP9_WpqAQ&start={x}'  
        HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                    'Accept-Language': 'pt-BR, pt;q=0.5'})
        request_result=requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(request_result.text,"html.parser")
        soup = str(soup)
        links_page = re.findall(r"(https:\/\/chat\.whatsapp\.com\/(invite\/)?[a-zA-Z0-9]{22})", soup) 
        x +=10
        for links in links_page:
            links = list(links)
            print(links[0])
            arquivo = open("content/links.txt", "a")
            arquivo.write(f"\n{links[0]}")
            

def scrapperOpt():

    url = input("Enter the website to extract the links:") 
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'pt-BR, pt;q=0.5'})
    request_result=requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(request_result.text,"html.parser")
    soup = str(soup)
    links_page = re.findall(r"(https:\/\/chat\.whatsapp\.com\/(invite\/)?[a-zA-Z0-9]{22})", soup) 

    for links in links_page:
        links = list(links)
        print(links[0])

def scrapperVal():
    print("You can validate the links you extracted or you can validate links by pasting the links in the content/links.txt file.")
    links = open('content/links.txt') 
    link = links.readlines()
    qtd = len(link) 
    i = 0

    while i <= qtd -1:
        url = link[i] 
        url = url[:-1] 
        HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                    'Accept-Language': 'pt-BR, pt;q=0.5'})
        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")
        dom = etree.HTML(str(soup))
        nome_grupo = (dom.xpath('//*[@id="main_block"]/h3')[0].text)
        arquivo = open("/content/links_valid.csv", "a") 
        if nome_grupo != None: 
            arquivo.write(f"{nome_grupo},{url}\n") 
        i +=1
