from django.contrib import admin
from .models import Post
# Register your models here.
# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
   list_details = ('title', 'slug', 'created_on', 'status')
   list_filter = ("status",)
   search_fields = ["title", "content"]
   prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
