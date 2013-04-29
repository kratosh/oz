from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="demo/index.html"), ),
    url(r'^knaan/$', TemplateView.as_view(template_name="demo/knaan.html"), ),
    url(r'^shlomit/$', TemplateView.as_view(template_name="demo/shlomit.html"), ),
)
