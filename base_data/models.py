from django.db import models

# Create your models here.

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to='card_images/', null=True)
    
 
    def __str__(self):
        return self.title
 
 
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
 
    def __str__(self):
        return self.name