from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from news.views import Like, Comments, Posts


# Register your models here.
User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'get_likes')
    search_fields = ('first_name', 'last_name')
    list_filter = []
    # print(UserAdmin.fieldsets)
    fieldsets = (
        ('Информация о пользователе', {'fields': ('first_name', 'last_name', 'get_likes')}),
        ('Коментарии', {
            'fields': ('get_comments',)}),
            )

    readonly_fields = ('first_name', 'last_name', 'get_likes', 'get_comments',)
        


    def get_likes(self, obj):
        user_likes = Like.objects.filter(author=obj).count()
        if user_likes:
            return user_likes
        else:
            return '-'

    def get_comments(self, obj):
        from django.utils.html import format_html
        print('dfsdfsf', obj)
        user_comments = Comments.objects.filter(author=obj)
        print('dfsdfsf', user_comments)
        if user_comments:
            code = '<table><tbody><tr><th>Пост</th><th>Коментарий</th></tr>'
            for i in user_comments:
                code +=f'<tr><td>{i.post.title}</td><td>{i.body}</td></tr>'
                print(i.post)
            return format_html(code + '</tbody></table>')
        else:
            return '-'

    

    get_likes.short_description = 'Кол-во лайков'
    get_comments.short_description = 'Коментарии'


# <table>
#     <tbody>
#         <tr>
#             <th>Volkswagen AG</th>
#             <th>Daimler AG</th>
#             <th>BMW Group</th>
#         </tr>
#         <tr>
#             <td>Lamborghini</td>
#             <td>Smart</td>
#             <td>Rolls-Royce</td>
#         </tr>
#     </tbody>
# </table>