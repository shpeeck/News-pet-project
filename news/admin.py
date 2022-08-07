from django.contrib import admin
from .models import Posts, Comments, Heading, Like

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_likes', 'get_comments')
    search_fields = ['title']
    list_filter = ['categories']
    # list_editable = ('title', 'released_year')
    exclude = ['likes', 'comments_post']
    fields = ('title', 'get_photo', 'body', 'image', 'categories',  'get_likes', 'get_comments')
    readonly_fields = ('get_photo', 'get_likes', 'get_comments')
    # fieldsets = ('get_photo',)
    # print(fields)
    print(admin.ModelAdmin.fieldsets)

    def get_likes(self, obj):
        user_likes = Like.objects.filter(post=obj).count()
        return user_likes

    def get_comments(self, obj):
        print(obj)
        user_comments = Comments.objects.filter(post=obj).count()
        return user_comments
    
    def get_photo(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="150">')

    get_likes.short_description = 'Кол-во лайков'
    get_comments.short_description = 'Коментарии'
    get_photo.short_description = 'Photo'


    class Meta:
        model = Posts


class CommentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comments._meta.fields]


class HeadingAdmin(admin.ModelAdmin):
    list_display = ['category_names']


admin.site.register(Posts, PostsAdmin)
# admin.site.register(Comments, CommentsAdmin)
admin.site.register(Heading, HeadingAdmin)

