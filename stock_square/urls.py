from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('stock_square_api.urls')),
]
