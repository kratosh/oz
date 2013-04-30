from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from oz.apps.sharedstate.views import GLOBAL_OBJECT_REPOSITORY

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="demo/index.html"), dict(
	    shared_states = GLOBAL_OBJECT_REPOSITORY,
    )),

    url(r'^knaan/$', TemplateView.as_view(template_name="demo/knaan.html")),
    url(r'^shlomit/$', TemplateView.as_view(template_name="demo/shlomit.html")),

	url(r'^shlomit/solve/$', TemplateView.as_view(template_name="demo/solve.html"), dict(
		background_image = "Shlomit_solve.gif", shared_states = GLOBAL_OBJECT_REPOSITORY,
	)),
	url(r'^knaan/solve/$', TemplateView.as_view(template_name="demo/solve.html"), dict(
		background_image = "Knaan_solve.gif", shared_states = GLOBAL_OBJECT_REPOSITORY,
	)),

)
