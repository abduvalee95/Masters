from django.db import models
from users.views import registerPage

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    date_of_birth = models.DateField(blank=True)
    formation = models.CharField(max_length=255,help_text='Образование')
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image_profile/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
