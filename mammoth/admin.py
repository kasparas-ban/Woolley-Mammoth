from django.contrib import admin
from mammoth.models import UserProfile, Pattern, Comment

class PatternAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text',)

admin.site.register(UserProfile)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Comment, CommentAdmin)