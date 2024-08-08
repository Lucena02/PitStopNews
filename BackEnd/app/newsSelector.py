import requests
from openai import OpenAI
from secret import *


client = OpenAI(
  api_key= OPEN_AI_KEY
)

testeSports= {
    "sample":[
        {"title": "The history-making Canadian swimming sensation experiencing a summer like no other", "score": 7},
        {"title": "USA gymnast Suni Lee talks viral podium photo", "score": 1},
        {"title": "Ukrainian Yaroslava Mahuchikh dedicates gold medal to fallen athletes, coaches", "score": 6},
        {"title": "Team USA`s `Clark Kent` pommel horse hero on how he prepares for routines", "score": 1},
        {"title": "This sport is making its Olympics debut in Paris. Just don`t call it breakdancing", "score": 8},
        {"title": "Harrison Butker of the Kansas City Chiefs reportedly becoming highest paid NFL kicker", "score": 10},
        {"title": "`This is not a transgender issue`: IOC addresses Olympic boxing controversy", "score": 8},
        {"title": "They are really quiet now: Biles on critics of her 2021 Olympics", "score": 6},
        {"title": "This Japanese skateboarder made Olympic history", "score": 0},
        {"title": "Simone Biles has nothing left to prove - to herself or anyone else", "score": 3}
    ]
}



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
    prompt = f"From all the news, give me only the 6 more important titles, judging by how important is the news title, considering objectiveness and not being clickbait and the importance of the news itself: \"{titles}\". Provide only the titles."
    
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            max_tokens=10
        )

        score = response['choices'][0]['message']['content'].strip()
        return score
    except Exception as e:
        print(f"An error occurred while scoring the title: {e}")
        return 0



def rank_and_select_top_news(fetched_titles):

    scored_news = score_title_with_gpt4(fetched_titles)

    return scored_news


fetched_titles = getNews()

# Rank and select the top 6 news articles
if fetched_titles:
    top_news = rank_and_select_top_news(fetched_titles)

    # Print the top 6 news articles
    print(top_news)
else:
    print("No news fetched.")

