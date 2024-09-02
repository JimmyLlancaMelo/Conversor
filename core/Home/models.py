from django.db import models

class fileYoutube(models.Model):

    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='fileYoutube/')

    def __str__(self):
        return self.title