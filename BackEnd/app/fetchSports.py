import requests
from bs4 import BeautifulSoup


dicionarioDesporto = {
    'titles': [],
    'images': [],
    'links': [],
    'source': []
}

def getSportsCNN():
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


getSportsCNN()
print(dicionarioDesporto)