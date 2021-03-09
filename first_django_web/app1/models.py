from django.db import models

# Create your models here.
# models.Model，这是Django的内置模型的基础类。
class Article(models.Model):
    headline = models.CharField(null = True, blank = True, max_length = 300)
    content = models.TextField(null = True, blank = True)
    def __str__(self):
        return self.headline