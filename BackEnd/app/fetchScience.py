import re
import requests
from bs4 import BeautifulSoup
from app.newsSelector import score_title_with_gpt4



def getScienceCNN(dicionarioScience):
    url = 'https://edition.cnn.com/science'


    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all headline elements with images.
        headlines = soup.find_all('div', class_='container_lead-plus-headlines-with-images__item')

        for headline in headlines:

            # Get the title
            title_tag = headline.find('span', class_='container__headline-text')
            if title_tag:
                dicionarioScience['titles'].append(title_tag.get_text(strip=True))                
            else:
                dicionarioScience['titles'].append("null")

            # Get the article link
            link_tag = headline.find('a', class_='container__link')
            if link_tag and 'href' in link_tag.attrs:
                stringg = "https://edition.cnn.com" + link_tag['href']
                dicionarioScience['links'].append(stringg)
            else:
                dicionarioScience['links'].append("null")


            image_tag = headline.find('img', class_='image__dam-img')
            if image_tag and 'src' in image_tag.attrs:
                dicionarioScience['images'].append(image_tag['src'])
            else:
                dicionarioScience['images'].append("null")

            dicionarioScience['sources'].append("CNN")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")





def getScienceBBC(dicionarioScience):
    url = 'https://www.bbc.com/innovation/science'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all headline elements with images.
        headlines = soup.find_all('div', {'data-testid': 'liverpool-card'})
        i = 0

        for headline in headlines:
            if i == 9 : break

            # Get the title
            title_tag = headline.find('h2', class_='bvDsJq')
            if title_tag:
                
                dicionarioScience['titles'].append(title_tag.get_text(strip=True))
            else:
                dicionarioScience['titles'].append("null")


            link_tag = headline.find('a', class_='gILusN')
            if link_tag != None and 'href' in link_tag.attrs:
                stringg = "https://www.bbc.com" + link_tag['href']
                dicionarioScience['links'].append(stringg)
            else:
                dicionarioScience['links'].append("null")



            responseTemp = requests.get(stringg)
            soup = BeautifulSoup(responseTemp.content, 'html.parser')
            img_tag = soup.find('img', class_='hIXOPW')
            if img_tag and 'src' in img_tag.attrs:
                dicionarioScience['images'].append(img_tag['src'])
            else:
                dicionarioScience['images'].append("null")


            dicionarioScience['sources'].append("BBC")
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


def fillDicScience():
    dicionarioScience = {
        'titles': [],
        'images': [],
        'links': [],
        'sources': []
    }
    getScienceCNN(dicionarioScience)
    getScienceBBC(dicionarioScience)
    top_news = score_title_with_gpt4(dicionarioScience['titles'])
    #print("AS MELHORES NOTICIAS DE POLITICA")
    #print(top_news)
    matches = re.findall(r'\d+\.\s(.*?)(?=\n\d+\.|$)', top_news)
    #print(matches)
    
    return fetchTitlesInDict(matches, dicionarioScience)


