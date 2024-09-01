import requests
from openai import OpenAI
from app.secret import *


client = OpenAI(
  api_key= OPEN_AI_KEY
)




def getNews():
    try:
        response = requests.get('http://127.0.0.1:5000/sports')
        response.raise_for_status()
        data = response.json()
        print(data['titles'])
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []



    
def score_title_with_gpt4(titles):
    #prompt = f"On a scale of 0 to 10, how important is the following news title: \"{title}\"? Provide only the score."
    prompt = f"From all the news, give me only the 6 more important titles, judging by how important is the news title, considering objectiveness and not being clickbait and the importance of the news itself: \"{titles}\". Don't include repeated news, or news that provide the same information. Provide only the titles without using quotation marks."
    
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            max_tokens=1000
        )

        score = response.choices[0].message.content.strip()
        return score
    except Exception as e:
        print(f"An error occurred while scoring the title: {e}")
        return 0





fetched_titles = getNews()

# Rank and select the top 6 news articles
if fetched_titles:
    top_news = score_title_with_gpt4(fetched_titles)

    # Print the top 6 news articles
    print(top_news)
else:
    print("No news fetched.")

