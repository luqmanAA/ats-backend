from django.contrib import admin

from .models import Author,Comment,Post
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class BlogAdmin(admin.ModelAdmin):
    list_filter = ('is_deleted',)
    model = Post
    list_display = ('title', 'post_date', 'author', 'slug')
    # fields = ('title', 'content', 'author')
    inlines = [CommentInline]
    

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ('username','email','first_name', 'last_name','number_of_posts')  
    ordering = ('id',)
    fields = ('username', 'slug', 'password', 'first_name', 'last_name', 'email', 'profile_image','bio', 'is_staff', 'groups')
    # exclude = ['is_superuser', 'user_permissions']  


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('short_description', 'post','comment_author', 'comment_time')


admin.site.register(Post, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)