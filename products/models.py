from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)   #not required, it can be empty
    
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False) #null=True  defualt=True

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_details', args=[str(self.id)])
        # return f'/products/details/{self.id}'

    # def get_absolute_url(self):
    #     return reverse("product_details", kwargs={"my_id": self.pk})
    
        