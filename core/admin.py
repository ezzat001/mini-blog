from django.contrib import admin
from .models import Posts
# Register your models here.
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "published"]
    #raw_id_fields = ["author"]
