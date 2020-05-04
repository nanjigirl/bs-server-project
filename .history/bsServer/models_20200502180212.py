from django.db import models

# Create your models here.

#创建模型类
class BookInfo(models.Model):
  title=models.CharField(max_length=10)
  pub_date=models.DateField()

class HeroInfo(models.Model):
  name=models.CharField(max_length=10)
  content=models.CharField(max_length=100)
  gender=models.CharField(default=True)
  