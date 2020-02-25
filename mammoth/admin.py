from django.contrib import admin
from mammoth.models import Category, Page, UserProfile, Pattern

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class PatternAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Pattern, PatternAdmin)
