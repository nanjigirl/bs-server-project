from django.db import models

# Create your models here.

#创建模型类
class User(models.Model):
  id = models.AutoField(primary_key = True) #该字段可不写，它会自动补全
  name = models.CharField(max_length = 30)
  age = models.IntegerField()
  sex = models.CharField(max_length = 2)

  def _str_(self):
    return "<User:{id=%s,name=%s,age=%s,sex=%s}>"

lass Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name