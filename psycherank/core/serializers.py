from rest_framework import serializers
from .models import User, UserQuestionnaire, UserAssessment, AssessmentQuestionnaire, Questionnaire, Assessment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # field = ["id", "name"]
        # exclude = ['id',]
        field = "__all__"


class UserQuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserQuestionnaire
        field = "__all__"


class UserAssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAssessment
        field = "__all__"


class AssessmentQuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssessmentQuestionnaire
        field = "__all__"


class QuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questionnaire
        field = "__all__"


class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assessment
        field = "__all__"
