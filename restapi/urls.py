from django.conf.urls import url
from .views import (
 UserViewSet,
)
urlpatterns = [
    url(r'^$',UserViewSet.as_view()),
    #url(r'^create/$',PostCreateViewSet.as_view()),
   # url(r'^all/$',PostIdViewSet.as_view()),
   # url(r'^comment/$',CommentIdViewSet.as_view()),
   # url(r'^comment/(?P<pk>\d+)/$',CommentIdViewSet.as_view()),
    
]