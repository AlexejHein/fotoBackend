from django.db import models


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('Mosel', 'Mosel'),
        ('Eifel', 'Eifel'),
        ('Hunsrück', 'Hunsrück'),
        ('Deutschland', 'Deutschland'),
        ('Architektur', 'Architektur'),
    ]
    title = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title or 'Bild'} ({self.category})"
