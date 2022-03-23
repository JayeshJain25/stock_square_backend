from rest_framework import serializers

from stock_square_api.model.news_model import NewsModel


class NewsDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ('title', 'source', 'description', 'publishedDate', 'url',
                  'photoUrl', 'readTime')
