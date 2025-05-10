from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PlayerImage(models.Model):
    player = models.ForeignKey(Product, related_name='extra_images', on_delete=models.CASCADE)
    descriptions = models.TextField(blank=True)
    title = models.TextField(blank=True)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.player.name}"
