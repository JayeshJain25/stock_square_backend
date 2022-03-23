import sys
from datetime import datetime

import pymongo
import readtime
from bs4 import BeautifulSoup
import requests
from celery import shared_task
from newspaper import Article
from newspaper import Config
from pymongo import UpdateOne


def MoneyControlNewsMethod():
    print("**** MoneyControlNewsMethod Started ****")
    client = pymongo.MongoClient('mongodb+srv://jayesh:uA3F4Zco25FklCcU@cluster0.uj7v6.mongodb.net/test?retryWrites'
                                 '=true&w=majority')
    db = client['stockSquare']
    collection_name = db['news']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    config.request_timeout = 30

    url = 'https://www.moneycontrol.com/news/business/markets/page-1'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find('ul', attrs={'id': 'cagetory'}).find_all('li', attrs={'class': 'clearfix'})
    lst = []
    try:
        for i in links:
            title = i.find('h2').text.strip()
            desc = i.find("p").text.strip()
            time = i.find("span").text.strip()
            new_time = datetime.strptime(time.split("IST")[0].strip(), '%B %d, %Y %I:%M %p').strftime(
                '%Y-%m-%d %H:%M') + ":00"
            urlLink = i.find('a')['href'].strip()
            image = i.find("img").attrs['data-src'].strip()
            source = "Moneycontrol"
            article = Article(urlLink, config=config)
            article.download()
            article.parse()
            article.nlp()
            read_time = readtime.of_text(article.text)
            summary = article.summary
            data = (title, desc, new_time, urlLink, image, source, read_time, summary)
            lst.append(data)
    except Exception:
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)
        print(error_type, 'Line:', error_info.tb_lineno)
        pass

    url = 'https://www.moneycontrol.com/news/business/markets/page-2'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find('ul', attrs={'id': 'cagetory'}).find_all('li', attrs={'class': 'clearfix'})
    try:
        for i in links:
            title = i.find('h2').text.strip()
            desc = i.find("p").text.strip()
            time = i.find("span").text.strip()
            new_time = datetime.strptime(time.split("IST")[0].strip(), '%B %d, %Y %I:%M %p').strftime(
                '%Y-%m-%d %H:%M') + ":00"
            urlLink = i.find('a')['href'].strip()
            image = i.find("img").attrs['data-src'].strip()
            source = "Moneycontrol"
            article = Article(urlLink, config=config)
            article.download()
            article.parse()
            article.nlp()
            read_time = readtime.of_text(article.text)
            summary = article.summary
            data = (title, desc, new_time, urlLink, image, source, read_time, summary)
            lst.append(data)
    except Exception:
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)
        print(error_type, 'Line:', error_info.tb_lineno)
        pass

    url = 'https://www.moneycontrol.com/news/business/markets/page-3'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find('ul', attrs={'id': 'cagetory'}).find_all('li', attrs={'class': 'clearfix'})
    try:
        for i in links:
            title = i.find('h2').text.strip()
            desc = i.find("p").text.strip()
            time = i.find("span").text.strip()
            new_time = datetime.strptime(time.split("IST")[0].strip(), '%B %d, %Y %I:%M %p').strftime(
                '%Y-%m-%d %H:%M') + ":00"
            urlLink = i.find('a')['href'].strip()
            image = i.find("img").attrs['data-src'].strip()
            source = "Moneycontrol"
            article = Article(urlLink, config=config)
            article.download()
            article.parse()
            article.nlp()
            read_time = readtime.of_text(article.text)
            summary = article.summary
            data = (title, desc, new_time, urlLink, image, source, read_time, summary)
            lst.append(data)
    except Exception:
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)
        print(error_type, 'Line:', error_info.tb_lineno)
        pass

    url = 'https://www.moneycontrol.com/news/business/markets/page-4'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find('ul', attrs={'id': 'cagetory'}).find_all('li', attrs={'class': 'clearfix'})
    try:
        for i in links:
            title = i.find('h2').text.strip()
            desc = i.find("p").text.strip()
            time = i.find("span").text.strip()
            new_time = datetime.strptime(time.split("IST")[0].strip(), '%B %d, %Y %I:%M %p').strftime(
                '%Y-%m-%d %H:%M') + ":00"
            urlLink = i.find('a')['href'].strip()
            image = i.find("img").attrs['data-src'].strip()
            source = "Moneycontrol"
            article = Article(urlLink, config=config)
            article.download()
            article.parse()
            article.nlp()
            read_time = readtime.of_text(article.text)
            summary = article.summary
            data = (title, desc, new_time, urlLink, image, source, read_time, summary)
            lst.append(data)
    except Exception:
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)
        print(error_type, 'Line:', error_info.tb_lineno)
        pass

    url = 'https://www.moneycontrol.com/news/business/markets/page-5'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find('ul', attrs={'id': 'cagetory'}).find_all('li', attrs={'class': 'clearfix'})
    try:
        for i in links:
            title = i.find('h2').text.strip()
            desc = i.find("p").text.strip()
            time = i.find("span").text.strip()
            new_time = datetime.strptime(time.split("IST")[0].strip(), '%B %d, %Y %I:%M %p').strftime(
                '%Y-%m-%d %H:%M') + ":00"
            urlLink = i.find('a')['href'].strip()
            image = i.find("img").attrs['data-src'].strip()
            source = "Moneycontrol"
            article = Article(urlLink, config=config)
            article.download()
            article.parse()
            article.nlp()
            read_time = readtime.of_text(article.text)
            data = (title, desc, image, urlLink, source, new_time, read_time)
            lst.append(data)
    except Exception:
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)
        print(error_type, 'Line:', error_info.tb_lineno)
        pass

    bulkOpList = []
    for item in lst:
        myquery = {"title": item[0]}
        newvalues = {
            "$set": {"title": item[0],
                     "description": item[1],
                     "photoUrl": item[2],
                     "url": item[3],
                     "source": item[4],
                     "publishedDate": item[5],
                     "readTime": str(item[6]),
                     }}
        bulkOpList.append(UpdateOne(myquery, newvalues, upsert=True))
    collection_name.bulk_write(bulkOpList)

    print("**** MoneyControlNewsMethod Ended ****")
