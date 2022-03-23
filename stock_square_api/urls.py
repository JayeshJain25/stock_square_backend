from django.conf.urls import url

from stock_square_api.view import news_view

urlpatterns = {
    url('news/news', news_view.get_news),
}
