from django.conf.urls import patterns, include, url
from oz.apps.sharedstate.views import set_state, update_state, get_state

# ajax for the poor
urlpatterns = patterns('',
    # set an object to some state
    url(r'^(?P<objname>[^/]+)/set/$', set_state),
    # update an object with some state (dict.update style)
    url(r'^(?P<objname>[^/]+)/update/$', update_state),
    # get the object state
    url(r'^(?P<objname>[^/]+)/get/$', get_state),
)
