from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Posts(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    content = models.TextField()
    posttime = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)

    