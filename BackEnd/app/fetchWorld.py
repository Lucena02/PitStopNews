import re
import requests
from bs4 import BeautifulSoup
from app.newsSelector import score_title_with_gpt4




def getWorldsCNN(dicionarioWorld):
    url = 'https://edition.cnn.com/world'


    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all headline elements with images.
        headlines = soup.find_all('div', class_='container_lead-plus-headlines__item')
        i = 0
        for headline in headlines:
            if i == 12 : break
            # Get the title
            title_tag = headline.find('span', class_='container__headline-text')
            if title_tag:
                dicionarioWorld['titles'].append(title_tag.get_text(strip=True))                
            else:
                dicionarioWorld['titles'].append("null")

            # Get the article link
            link_tag = headline.find('a', class_='container__link')
            if link_tag and 'href' in link_tag.attrs:
                stringg = "https://edition.cnn.com" + link_tag['href']
                dicionarioWorld['links'].append(stringg)
            else:
                dicionarioWorld['links'].append("null")

            responseTemp = requests.get(stringg)
            soup = BeautifulSoup(responseTemp.content, 'html.parser')
            img_tag = soup.find('img', class_='image__dam-img')
            if img_tag and 'src' in img_tag.attrs:
                dicionarioWorld['images'].append(img_tag['src'])
            else:
                dicionarioWorld['images'].append("null")


            dicionarioWorld['sources'].append("CNN")
            i+=1

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



def getWorldBBC(dicionarioWorld):
    url = 'https://www.bbc.com/news'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all headline elements with images.
        #headlines = soup.find_all('div', class_="dyVGhC")
        #headlines.append(soup.find_all('div', class_="hprnWz"))
        headlines = soup.find_all('div', {'data-testid': 'cambridge-card'})
        i = 0
        print(headlines)

        for headline in headlines:
            if i == 15 : break

            # Get the title
            title_tag = headline.find('h2', class_='gJvjEE')
            if title_tag:
                
                dicionarioWorld['titles'].append(title_tag.get_text(strip=True))
            else:
                dicionarioWorld['titles'].append("null")


            link_tag = headline.find('a', class_='gILusN')
            if link_tag != None and 'href' in link_tag.attrs:
                stringg = "https://www.bbc.com" + link_tag['href']
                dicionarioWorld['links'].append(stringg)
            else:
                dicionarioWorld['links'].append("null")


            print(stringg)
            responseTemp = requests.get(stringg)
            soup = BeautifulSoup(responseTemp.content, 'html.parser')
            img_tag = soup.find('img', class_='hIXOPW')
            if img_tag and 'src' in img_tag.attrs:
                dicionarioWorld['images'].append(img_tag['src'])
            else:
                dicionarioWorld['images'].append("null")

            print("TESTEEEEEEEEEEEE")
            dicionarioWorld['sources'].append("BBC")
            i+=1

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



def fetchTitlesInDict(titles, dicionarioPolitics):
    dicionarioPoliticsFinal = {
        'titles': [],
        'images': [],
        'links': [],
        'sources': []
    }
    for titulo in titles:
        for i, item in enumerate(dicionarioPolitics['titles']):
            item = item.replace('\xa0', ' ').strip()
            #print("\n")
            titulo = titulo.rstrip()
            #print(repr(titulo))
            #print(repr(item))
            if titulo == item:
                print("IGUAL")
                dicionarioPoliticsFinal['titles'].append(dicionarioPolitics['titles'][i])
                dicionarioPoliticsFinal['images'].append(dicionarioPolitics['images'][i])
                dicionarioPoliticsFinal['links'].append(dicionarioPolitics['links'][i])
                dicionarioPoliticsFinal['sources'].append(dicionarioPolitics['sources'][i])
                break

    return dicionarioPoliticsFinal


def fillDicWorld():
    dicionarioWorld = {
        'titles': [],
        'images': [],
        'links': [],
        'sources': []
    }
    getWorldsCNN(dicionarioWorld)
    getWorldBBC(dicionarioWorld)
    top_news = score_title_with_gpt4(dicionarioWorld['titles'])
    #print("AS MELHORES NOTICIAS DE POLITICA")
    #print(top_news)
    matches = re.findall(r'\d+\.\s(.*?)(?=\n\d+\.|$)', top_news)
    #print(matches)
    
    return fetchTitlesInDict(matches, dicionarioWorld)

