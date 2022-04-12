from django.urls import path, include
from django.views.decorators.cache import cache_page
from . import views
urlpatterns = [
path('chat_data',views.chat_bot),
path('data',views.chat_detail),

]
