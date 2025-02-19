from django.urls import path
from .views import GalleryImageList

urlpatterns = [
    path('', GalleryImageList.as_view(), name='gallery-image-list'),
]
