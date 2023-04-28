from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Book(models.Model):
    title  = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, default=None)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length = 2083, default="https://pngimg.com/uploads/book/book_PNG2111.png")
    follow_author = models.CharField(max_length=2083, blank=True)  
    book_available = models.BooleanField(default=True)
    upload_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
	product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.title
