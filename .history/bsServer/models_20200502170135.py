from django.db import models

# Create your models here.

#创建模型类
class User(models.Model):
  id = models.AutoField(primary_key = True) #