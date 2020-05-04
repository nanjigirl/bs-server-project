from django.contrib import admin
from bsServer.models import BookInfo,HeroInfo
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
  list_display = []

admin.site.register(BookInfo)
admin.site.register(HeroInfo)