from django.db import models

class TreePost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()  
    buy_url = models.URLField()  
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
