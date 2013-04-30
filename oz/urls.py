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
