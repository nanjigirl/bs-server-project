from django.contrib import admin
from bsServer.models import BookInfo,HeroInfo
# Register your models here.

class BookInfoAdmin(admin.ModelAd)
admin.site.register(BookInfo)
admin.site.register(HeroInfo)