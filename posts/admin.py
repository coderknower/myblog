from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","timestamp","updated","title"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title","content"]
    list_editable = ["title"]
    class Meta:
        model = Post



admin.site.register(Post, PostModelAdmin)

# Register your models here.
