from django.contrib import admin
from mammoth.models import Category, Page, UserProfile, Pattern,Comment

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class PatternAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_type',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Comment,CommentAdmin)