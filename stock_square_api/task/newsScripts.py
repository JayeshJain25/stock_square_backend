import pymongo
import readtime
import requests
import pandas as pd
from datetime import  timedelta, datetime

from celery import shared_task
from newspaper import Config

from newspaper import Article
from pymongo import UpdateOne


def NewsScriptsMethod():
    print("**** NewsScriptsMethod Started ****")

    client = pymongo.MongoClient('mongodb+srv://jayesh:uA3F4Zco25FklCcU@cluster0.uj7v6.mongodb.net/test?retryWrites'
                                 '=true&w=majority')
    db = client['stockSquare']
    collection_name = db['news']

    url = 'https://newsapi.org/v2/everything?'

    api_key = "441d1787a331477a858d7d9c0b07d4bb"

    # date = date.today()
    date = datetime.now() - timedelta(days=7)

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    config.request_timeout = 30

    news_parameters = {
        'q': 'india stock market news',
        'page': '1',
        'pageSize': '100',
        'from': date,
        'sortBy': 'publishedAt',
        'apiKey': '441d1787a331477a858d7d9c0b07d4bb',
        'language': 'en'
    }
    news = requests.get(url, params=news_parameters)
    news = news.json()

    news_articles = news['articles']

    def get_articles(file):
        article_results = []

        for i in range(len(file)):
            newTimeArray = file[i]['publishedAt'].split("T")
            newTime = newTimeArray[0] + " " + newTimeArray[1].split("Z")[0]

            article_dict = {'title': file[i]['title'], 'source': file[i]['source'],
                            'description': file[i]['description'],
                            'content': file[i]['content'], 'pub_date': newTime, 'url': file[i]["url"],
                            'photo_url': file[i]['urlToImage']}

            article_results.append(article_dict)
        return article_results

    news_df = pd.DataFrame(get_articles(news_articles))

    def source_getter(df):
        source = []
        for source_dict in df['source']:
            source.append(source_dict['name'])

        df['source'] = source

    def get_article_estimate_time(df):
        estimated_time = []

        for url1 in df['url']:
            article = Article(url1, config=config)
            try:
                article.download()
                article.parse()
                article.nlp()
                result = readtime.of_text(article.text)
                estimated_time.append(result.text)
            except:
                estimated_time.append("unknown")
                pass

        df['read_time'] = estimated_time

    get_article_estimate_time(news_df)
    source_getter(news_df)

    bulkOpList = []
    for item in news_df.index:
        myquery = {"title": news_df['title'][item]}
        newvalues = {
            "$set": {"title": news_df['title'][item],
                     "description": news_df['description'][item],
                     "photoUrl": news_df['photo_url'][item],
                     "url": news_df['url'][item],
                     "source": news_df['source'][item],
                     "publishedDate": str(news_df['pub_date'][item]),
                     "readTime": str(news_df['read_time'][item]),
                     }}
        bulkOpList.append(UpdateOne(myquery, newvalues, upsert=True))
    collection_name.bulk_write(bulkOpList)
    print("**** NewsScriptsMethod Ended ****")
