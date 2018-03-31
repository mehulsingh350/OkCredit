from django.conf.urls import url
from rest_framework.authtoken import views
from webapp.views import SnippetList

app_name='webapp'

urlpatterns=[
	url(r'^getlist/$',SnippetList.as_view(),name='getlist'),
]