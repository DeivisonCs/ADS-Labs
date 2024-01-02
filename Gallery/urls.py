from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_posts, name='gallery_posts'),
    path('/album/', views.view_album, name='view_album'),
    path('Gallery/New_Album', views.new_album, name='new_album'),
]
