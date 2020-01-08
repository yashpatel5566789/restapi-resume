from django.conf.urls import url
from .views import (
 UserViewSet,
 ProfileViewSet,
 ResumeViewSet,
 WorkExperienceViewSet,
 CertificationViewSet,
 EducationViewSet,
 SkillViewSet,
 LanguageViewSet,
)
urlpatterns = [
    url(r'^$',UserViewSet.as_view()),
    url(r'^profile/$',ProfileViewSet.as_view()),
    url(r'^resume/$',ResumeViewSet.as_view()),
    url(r'^work/$',WorkExperienceViewSet.as_view()),
    url(r'^certification/$',CertificationViewSet.as_view()),
    url(r'^education/$',EducationViewSet.as_view()),
    url(r'^skill/$',SkillViewSet.as_view()),
    url(r'^language/$',LanguageViewSet.as_view()),
   # url(r'^all/$',PostIdViewSet.as_view()),
   # url(r'^comment/$',CommentIdViewSet.as_view()),
   # url(r'^comment/(?P<pk>\d+)/$',CommentIdViewSet.as_view()),
    
]