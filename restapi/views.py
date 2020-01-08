from django.shortcuts import render
from rest_framework import generics, mixins
from .models import (
    User, 
    Profile, 
    Resume, 
    WorkExperience,
    Certification, 
    Education, 
    Skill,
    Language,
     )   
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    ResumeSerializer,
    WorkExperienceSerializer,
    CertificationSerializer,
    EducationSerializer,
    SkillSerializer,
    LanguageSerializer,
)
# Create your views here.
class UserViewSet(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes        = []
    authentication_classes    = []
    serializer_class = UserSerializer
    
    def get_queryset(self):
        qs = User.objects.all()
        query = self.request.GET.get('a')
        if query is not None:
           qs =qs.filter(query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj=None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return self.retrieve(request,*args, **kwargs )
        return super().get(request,*args, **kwargs )

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)