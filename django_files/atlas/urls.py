#from django.conf.urls import patterns, include
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
	# internationalization ######################################################
	(r'^i18n/', include('django.conf.urls.i18n')),
	(r'^set_language/(?P<lang>[a-z-]{2,5})/$', 'atlas.languages.set_language'),

	# general site ##############################################################
	(r'^$', 'observatory.views.home'),
	
	# about section
	(r'^about/$', 'observatory.views.about'),
	(r'^about/blog/$', "blog.views.blog_index"),
	(r'^about/team/$', "observatory.views.team"),
	(r'^about/permissions/$', "observatory.views.permissions"),
	
	# book
	(r'^book/$', 'observatory.views.book'),
	
	# API #######################################################################
	# (r'^api/$', 'observatory.views.api'),
	(r'^api/$', redirect_to, {'url': 'http://web.media.mit.edu/~simoes/embed/'}),
	
	# Explore (App) #############################################################
	# Legacy app redirect
	(r'^app/(?P<app_name>[a-z0-9_]+)/(?P<trade_flow>\w{6,10})/(?P<filter>[a-z0-9\.]+)/(?P<year>[0-9\.]+)/$', 'observatory.views.app_redirect'),
	
	# New app URL structure
	(r'^explore/$', redirect_to, {'url': '/explore/tree_map/export/usa/all/show/2009/'}),
	(r'^explore/(?P<app_name>[a-z_]+)/(?P<trade_flow>\w{6,10})/(?P<country1>\w{3,4})/(?P<country2>\w{3,4})/(?P<product>\w{3,4})/(?P<year>[0-9\.]+)/$', 'observatory.views.explore'),
	
	# Embed URL
	(r'^embed/(?P<app_name>[a-z_]+)/(?P<trade_flow>\w{6,10})/(?P<country1>\w{3,4})/(?P<country2>\w{3,4})/(?P<product>\w{3,4})/(?P<year>[0-9\.]+)/$', 'observatory.views.embed'),

	# API ########################################################################
	(r'^api/(?P<trade_flow>[a-z_]{6,10})/(?P<country1>\w{3})/all/show/(?P<year>[0-9\.]+)/$', 'observatory.views.api_casy'),
	(r'^api/(?P<trade_flow>[a-z_]{6,10})/(?P<country1>\w{3})/show/all/(?P<year>[0-9\.]+)/$', 'observatory.views.api_csay'),
	(r'^api/(?P<trade_flow>[a-z_]{6,10})/(?P<country1>\w{3})/(?P<country2>\w{3})/show/(?P<year>[0-9\.]+)/$', 'observatory.views.api_ccsy'),
	(r'^api/(?P<trade_flow>[a-z_]{6,10})/(?P<country1>\w{3})/show/(?P<product>\w{4})/(?P<year>[0-9\.]+)/$', 'observatory.views.api_cspy'),
	(r'^api/(?P<trade_flow>[a-z_]{6,10})/show/all/(?P<product>\w{4})/(?P<year>[0-9\.]+)/$', 'observatory.views.api_sapy'),
)
