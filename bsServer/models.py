from django.db import models

# Create your models here.

# 创建模型类


class BookInfo(models.Model):
    title = models.CharField(max_length=10)
    pub_date = models.DateField()

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    book = models.ForeignKey(BookInfo, to_field='id', on_delete=models.CASCADE)

class PotentialInfo(models.Model):
    ProtectionPotential = models.FloatField(max_length=10)
    lastTime = models.DateTimeField(auto_now=True)