from django.conf.urls import patterns, url

from Seamless_Accounting import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^/home/$', views.home, name='home'),
	url(r'^/upload_inventory/$', views.home, name='upload_inventory'),
	url(r'^/billing/$', views.home, name='billing'),
	url(r'^/view_profit/$', views.home, name='view_profit'),
	url(r'^/upload_expenditure/$', views.home, name='upload_expenditure'),
	url(r'^/upload_savings/$', views.home, name='upload_savings'),
	url(r'^/calculate_tax/$', views.home, name='calculate_tax'),
)
	
