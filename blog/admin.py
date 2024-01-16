from django.contrib import admin
from .models import Post, Comment, About, Category
from django_summernote.admin import SummernoteModelAdmin
from .models import CollaborateRequest

# Register your models here.

# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ['name', 'description']
    list_filter = ('name', 'description')
    readonly_fields = ('id',)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'content')
    summernote_fields = ('content',)

# COLLABORATE REQUEST FORM

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'read')
    search_fields = ['name', 'email']
    list_filter = ('name', 'email')


