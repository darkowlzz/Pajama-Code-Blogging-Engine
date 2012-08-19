from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
