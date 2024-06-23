from django.db import models

# Create your models here.

class News(models.Model):
    type_news = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    date = models.DateField()
    time = models.TimeField()
    titre = models.CharField(max_length=500)
    text = models.TextField()

    def __str__(self):
        return self.titre
