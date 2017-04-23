from django.conf.urls import url
from . import views

urlpattersn = [
	url(r'^$', views.post_list, name='post_list'),]