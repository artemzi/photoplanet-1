from django.contrib import admin

from photoplanet.models import Photo
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'email', 'created_at')
    list_display_links = ('__unicode__', 'name', 'email')
    readonly_fields = ['created_at', ]
    class Meta:
        model = Feedback

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'username', 'like_count', 'vote_count', 'created_time')
    list_display_links = ('__unicode__', 'username', 'like_count', 'vote_count')
    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Feedback, FeedbackAdmin)
