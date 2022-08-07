from django.contrib import admin
from .models import Posts, Comments, Heading

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Posts._meta.fields]
    # search_fields = ['id', 'title', 'released_year', 'author_id']
    # list_filter = ['author_id']
    # list_editable = ('title', 'released_year')
    exclude = ['likes', 'comments_post']

    class Meta:
        model = Posts


class CommentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comments._meta.fields]


class HeadingAdmin(admin.ModelAdmin):
    list_display = ['category_names']


admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Heading, HeadingAdmin)

