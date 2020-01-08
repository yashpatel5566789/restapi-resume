from django.contrib import admin
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
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Resume)
admin.site.register(WorkExperience)
admin.site.register(Certification)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Language)

