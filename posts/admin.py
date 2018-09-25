from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ('title','timestamp','updated')
  class Meta:
    model = Post
    

admin.site.register(Post, PostAdmin)




