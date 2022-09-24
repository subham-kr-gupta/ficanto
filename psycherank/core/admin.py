from django.contrib import admin

# Register your models here.
from .models import User, Assessment, Questionnaire, UserQuestionnaire, UserAssessment, AssessmentQuestionnaire, CorporateUser

admin.site.register(User)
admin.site.register(Assessment)
admin.site.register(Questionnaire)
admin.site.register(UserAssessment)
admin.site.register(UserQuestionnaire)
admin.site.register(AssessmentQuestionnaire)
admin.site.register(CorporateUser)
