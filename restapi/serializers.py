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
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['created_at', 'updated_at']
        
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
   # users_set = UserSerializer(many=True)
    class Meta:
        model = Resume
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    #resumes_set = ResumeSerializer(many=True)
    class Meta:
        model = WorkExperience
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    #resumes_set = ResumeSerializer(many=True)
    class Meta:
        model = Certification
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    #resumes_set = ResumeSerializer(many=True)
    class Meta:
        model = Education
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    #resumes_set = ResumeSerializer(many=True)
    class Meta:
        model = Skill
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
   # resumes_set = ResumeSerializer(many=True)
    class Meta:
        model = Language
        fields = '__all__'





