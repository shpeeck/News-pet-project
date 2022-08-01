from django.contrib import admin
from .models import Posts

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Posts._meta.fields]
    # search_fields = ['id', 'title', 'released_year', 'author_id']
    # list_filter = ['author_id']
    # list_editable = ('title', 'released_year')

    class Meta:
        model = Posts

admin.site.register(Posts, PostsAdmin)