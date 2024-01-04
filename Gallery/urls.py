from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_posts, name='gallery_posts'),
    path('/view', views.view_album, name='view_album'),
    path('/remove', views.remove_album, name='remove_album'),
    path('Gallery/New_Album', views.new_album, name='new_album'),
]
