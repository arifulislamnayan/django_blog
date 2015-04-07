from django.contrib import admin
from blog.models import *



class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "body", "created_at")
	search_fields =['title']



admin.site.register(Post,PostAdmin)















# Register your models here