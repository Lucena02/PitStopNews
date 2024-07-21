import requests
from bs4 import BeautifulSoup


dicionarioPolitics = {
    'titles': [],
    'images': [],
    'links': [],
    'sources': []
}

def getPoliticsCNN():
    url = 'https://edition.cnn.com/politics'


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
                dicionarioPolitics['titles'].append(title_tag.get_text(strip=True))                
            else:
                dicionarioPolitics['titles'].append("null")

            # Get the article link
            link_tag = headline.find('a', class_='container__link')
            if link_tag and 'href' in link_tag.attrs:
                stringg = "https://edition.cnn.com" + link_tag['href']
                dicionarioPolitics['links'].append(stringg)
            else:
                dicionarioPolitics['links'].append("null")

            responseTemp = requests.get(stringg)
            soup = BeautifulSoup(responseTemp.content, 'html.parser')
            img_tag = soup.find('img', class_='image__dam-img')
            if img_tag and 'src' in img_tag.attrs:
                dicionarioPolitics['images'].append(img_tag['src'])
            else:
                dicionarioPolitics['images'].append("null")


            dicionarioPolitics['sources'].append("CNN")
            i+=1

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


getPoliticsCNN()
print(dicionarioPolitics)