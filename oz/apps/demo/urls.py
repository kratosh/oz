from django.conf.urls import patterns, include, url
from views import UserView

urlpatterns = patterns('',
    url(r'^user/(?P<name>[^/]+)/$', UserView.as_view()),
)
