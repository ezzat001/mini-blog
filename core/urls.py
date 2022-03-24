from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api',PostsViewSet)
urlpatterns = [
    path('', index), 
    path('logout',logoutview),
    path('<int:id>', post_detail),
    path('<str:userid>-posts',author_posts),
    path('',include(router.urls)),
    path('<int:id>',include(router.urls)),   
]