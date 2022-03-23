import re

import pymongo
from django.http import JsonResponse
from rest_framework.decorators import api_view

from stock_square_api.serializer.news_data_serializers import NewsDataListSerializer
from stock_square_api.task import IPO, moneycontrol, newsScripts


@api_view(['GET'])
def get_news(request):
    client = pymongo.MongoClient('mongodb+srv://jayesh:uA3F4Zco25FklCcU@cluster0.uj7v6.mongodb.net/test?retryWrites'
                                 '=true&w=majority')
    db = client['stockSquare']
    collection_name = db['news']

    data = list(collection_name.find(allow_disk_use=True).sort('publishedDate', pymongo.DESCENDING))

    newNewsList = []
    titleList = []

    for i in range(len(data)):
        if data[i]['title'] is None:
            var = ""
        else:
            var = data[i]['title']
        titleList.append(var)

        newNewsList.append(
            {"_id": data[i]['_id'], "title": var.strip(), "source": data[i]['source'],
             "description": data[i]['description'],
             "publishedDate": data[i]['publishedDate'],
             "url": data[i]['url'],
             "photoUrl": data[i]['photoUrl'], "readTime": data[i]['readTime'], })

    res = []
    for i in range(len(titleList)):
        if ''.join(char for char in titleList[i].split("-")[0].lower().strip() if char.isalnum()) not in res:
            res.append(''.join(char for char in titleList[i].split("-")[0].lower().strip() if char.isalnum()))

    updatedNewsList = []
    for i in range(len(newNewsList)):
        if ''.join(char for char in newNewsList[i]['title'].split("-")[0].lower().strip() if char.isalnum()) in res:
            res.remove(
                ''.join(char for char in newNewsList[i]['title'].split("-")[0].lower().strip() if char.isalnum()))
            updatedNewsList.append(newNewsList[i])

    tutorials_serializer = NewsDataListSerializer(updatedNewsList, many=True)
    return JsonResponse(tutorials_serializer.data,
                        safe=False)


def IPONewsToDB(self):
    IPO.IPONewsMethod()


def MoneyControlNewsToDB(self):
    moneycontrol.MoneyControlNewsMethod()


def NewsScriptsToDB(self):
    newsScripts.NewsScriptsMethod()
