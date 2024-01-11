from django.contrib import admin
from .models import Post, Comment, About
from django_summernote.admin import SummernoteModelAdmin
from .models import CollaborateForm

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
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

@admin.register(CollaborateForm)
class CollaborateFormAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
