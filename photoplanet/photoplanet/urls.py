from django.conf.urls import include, patterns, url
from django.conf import settings
from django.views.generic import TemplateView

from .views import (
    HomePhotosListView, AllPhotosListView,
    PhotoDetailView, PhotoVoteView,
    PhotoDayArchiveView)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
print 'autodiscovered'


urlpatterns = patterns(
    'photoplanet.views',
    url(r'^$', HomePhotosListView.as_view(), name='home'),
    url(r'^all/$', AllPhotosListView.as_view(), name='all'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
        PhotoDayArchiveView.as_view(),
        name="photo-date-view"),
    url(r'^all/$', AllPhotosListView.as_view(), name='all'),
    url(r'^photo/(?P<pk>\w+)/$', PhotoDetailView.as_view(), name='photo-detail'),
    url(r'^photo/(?P<pk>\w+)/vote$', PhotoVoteView.as_view(), name='photo-vote'),
    url(r'^load_photos/$', 'load_photos', name='load-photos'),
    url(r'^about/$', TemplateView.as_view(template_name='photoplanet/about.html'), name='about'),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feedback/', include('feedback.urls')),
    url(r'', include('users.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout')
)

# http://stackoverflow.com/questions/9047054/heroku-handling-static-files-in-django-app
# TODO: needs to be removed this is temporary to have static served from HEROKU
urlpatterns += patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
