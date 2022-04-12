from django.urls import path, include
from django.views.decorators.cache import cache_page
from . import views
urlpatterns = [
path('',views.home),
path('meet-choach',views.meet_choach),
path('podcast',views.podcast),
path('services',views.our_service),
path('blog',views.blog),
path('press',views.press),
path('resources',views.resources),
path('contact',views.contact),
path('services/<str:nm>,<int:id>',views.services_details),
path('blog/<str:title>,<int:id>', views.blog_details),

]
