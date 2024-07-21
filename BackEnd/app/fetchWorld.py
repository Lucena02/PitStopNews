import requests
from bs4 import BeautifulSoup


dicionarioWorld = {
    'titles': [],
    'images': [],
    'links': [],
    'sources': []
}

def getWorldsCNN():
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
                print(stringg)
                dicionarioWorld['links'].append(stringg)
            else:
                dicionarioWorld['links'].append("null")

            responseTemp = requests.get(stringg)
            soup = BeautifulSoup(responseTemp.content, 'html.parser')
            img_tag = soup.find('img', class_='image__dam-img')
            if img_tag and 'src' in img_tag.attrs:
                image_url = img_tag['src']
                print(f"Image URL: {image_url}")
            else:
                print("No image found with the specified class.")


            dicionarioWorld['sources'].append("CNN")
            i+=1

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


getWorldsCNN()
print(dicionarioWorld)