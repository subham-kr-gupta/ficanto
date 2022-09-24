from dataclasses import field
from rest_framework import serializers
from .models import User, UserQuestionnaire, UserAssessment, AssessmentQuestionnaire, Questionnaire, Assessment, CorporateUser


class CorporateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CorporateUser
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # field = ["id", "name"]
        exclude = ['password',]
        # field = "__all__"


class UserQuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserQuestionnaire
        fields = "__all__"


class UserAssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAssessment
        fields = "__all__"


class AssessmentQuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssessmentQuestionnaire
        fields = "__all__"


class QuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questionnaire
        fields = "__all__"


class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assessment
        fields = "__all__"
