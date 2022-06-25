from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"id": self.pk})

    # def get_absolute_url(self):   
    #     return reverse("product_details", kwargs={"my_id": self.pk})


class Post(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #Note, timezone.now was passed as agrs not called as function - timezone.now()
                        # Args for DateTimeField - auto_now = True for time add, but best for time for post update
                        #                            auto_now_add = True for when the object is created, but still not the best. Read more

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    