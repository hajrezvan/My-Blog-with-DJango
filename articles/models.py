from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # blank = True برای اینکه بتوانیم اگر هیچ عکسی رو نخواستیم بذاریم، مقدارش خالی باشه
    image = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'
