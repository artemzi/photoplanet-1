from django.contrib import admin

from photoplanet.models import Photo
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'email', 'created_at', 'timestamp')
    list_display_links = ('__unicode__', 'name', 'email')
    readonly_fields = ['created_at', ]
    class Meta:
        model = Feedback


admin.site.register(Photo)
admin.site.register(Feedback, FeedbackAdmin)
