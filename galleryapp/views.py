from rest_framework import generics
from .models import GalleryImage
from .serializers import GalleryImageSerializer


class GalleryImageList(generics.ListAPIView):
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        queryset = GalleryImage.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)
        return queryset
