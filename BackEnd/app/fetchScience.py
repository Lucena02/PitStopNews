import requests
from bs4 import BeautifulSoup




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
                print(stringg)
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

def fillDicScience():
    dicionarioScience = {
        'titles': [],
        'images': [],
        'links': [],
        'sources': []
    }
    getScienceCNN(dicionarioScience)
    return dicionarioScience