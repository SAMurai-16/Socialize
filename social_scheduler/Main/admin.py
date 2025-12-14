from django.contrib import admin
from .models import ScheduledPost, Telegram, Reddit, RedditAccount, ContentTemplate

# Register your models here.


@admin.register(ScheduledPost)
class ScheduledPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'platfrom',  'scheduled_time', 'status')


@admin.register(ContentTemplate)
class ContentTemplateAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_type', 'topic', 'tone', 'created_at')
    list_filter = ('content_type', 'tone', 'created_at')
    search_fields = ('topic', 'audience', 'keywords')
    readonly_fields = ('created_at',)


admin.site.register(Telegram)
admin.site.register(Reddit)
admin.site.register(RedditAccount)

