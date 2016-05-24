"""urls."""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TutorDetail, TutorList

urlpatterns = [

	url(r'^$', TutorList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', TutorDetail.as_view()),
    #url(r'^register/$', register),


]

urlpatterns = format_suffix_patterns(urlpatterns)
