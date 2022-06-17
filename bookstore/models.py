from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, blank=True, null = True)
    author = models.CharField(max_length=100)
    released_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 100.00)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_book", kwargs={"book_id": self.pk})
    
    
