import requests
from bs4 import BeautifulSoup



def getSportsCNN(dicionarioDesporto):
    url = 'https://edition.cnn.com/sport'


    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all headline elements with images.
        headlines = soup.find_all('div', class_='container_lead-plus-headlines-with-images__item')

        for headline in headlines:

            # Get the title
            title_tag = headline.find('span', class_='container__headline-text')
            if title_tag:
                dicionarioDesporto['titles'].append(title_tag.get_text(strip=True))                
            else:
                dicionarioDesporto['titles'].append("null")

            # Get the article link
            link_tag = headline.find('a', class_='container__link')
            if link_tag and 'href' in link_tag.attrs:
                stringg = "https://edition.cnn.com" + link_tag['href']
                print(stringg)
                dicionarioDesporto['links'].append(stringg)
            else:
                dicionarioDesporto['links'].append("null")


            image_tag = headline.find('img', class_='image__dam-img')
            if image_tag and 'src' in image_tag.attrs:
                dicionarioDesporto['images'].append(image_tag['src'])
            else:
                dicionarioDesporto['images'].append("null")

            dicionarioDesporto['sources'].append("CNN")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



def getSportsBBC(dicionarioDesporto):
    url = 'https://www.bbc.com/sport'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all headline elements with images.
        headlines = soup.find_all('li', class_='e1gp961v0')
        i = 0

        for headline in headlines:
            if i == 12 : break

            # Get the title
            title_tag = headline.find('p', class_='exn3ah96')
            if title_tag:
                
                dicionarioDesporto['titles'].append(title_tag.get_text(strip=True))
            else:
                dicionarioDesporto['titles'].append("null")

            # Get the article link
            link_tag = headline.find('a', class_='exn3ah91')
            if link_tag != None and 'href' in link_tag.attrs:
                stringg = "https://www.bbc.com" + link_tag['href']
                dicionarioDesporto['links'].append(stringg)
            else:
                dicionarioDesporto['links'].append("null")

            responseTemp = requests.get(stringg)
            soup = BeautifulSoup(responseTemp.content, 'html.parser')
            img_tag = soup.find('img', class_='edrdn950')
            if img_tag and 'src' in img_tag.attrs:
                dicionarioDesporto['images'].append(img_tag['src'])
            else:
                dicionarioDesporto['images'].append("null")


            dicionarioDesporto['sources'].append("BBC")
            i+=1

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



def fillDicSports():   
    dicionarioDesporto = {
        'titles': [],
        'images': [],
        'links': [],
        'sources': []
    }
    getSportsCNN(dicionarioDesporto)
    getSportsBBC(dicionarioDesporto)
    return dicionarioDesporto
