from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # default app is demo
    url(r'^$', RedirectView.as_view(url='/demo/')),
    # url(r'^oz/', include('oz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^demo/', include('oz.apps.demo.urls')),
    url(r'^sharedstate/', include('oz.apps.sharedstate.urls')),
)

# support static files in heroku when not in debug
# source: http://stackoverflow.com/questions/9047054/heroku-handling-static-files-in-django-app
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )