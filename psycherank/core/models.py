from signal import valid_signals
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models


class CorporateUser(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    def __str__(self) -> str:
        return self.name


class User(models.Model):
    user_choices = (('NORMAL', 'NORMAL'), ('CORPORATE', 'CORPORATE'))
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=True, default='')
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=500, blank=False)
    is_email_verified = models.BooleanField(default=False)
    phone_number = models.PositiveBigIntegerField(blank=True, null=True)
    is_phone_verified = models.BooleanField(default=False)
    year_of_experience = models.FloatField(default=0)
    resume = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=100, choices=user_choices, default='NORMAL')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    corporate_id = models.ForeignKey(CorporateUser, on_delete=models.SET_NULL, blank=True, null=True)
    # last_login = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.email


class Assessment(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    duration = models.IntegerField()  # Save time in minutes
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # OR CASCADE
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # corporate_id = models.ForeignKey(CorporateUser, on_delete=models.CASCADE) # Need to Confirm with Brijesh
    
    def __str__(self) -> str:
        return self.name


class Questionnaire(models.Model):
    name = models.TextField(max_length=1000)
    options = models.JSONField()  # ArrayField in case of any issue
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # corporate_id = models.ForeignKey(CorporateUser, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name


class AssessmentQuestionnaire(models.Model):
    assessment_id = models.ForeignKey(Assessment, on_delete=models.DO_NOTHING)
    question_id = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (('assessment_id', 'question_id'),)
        
    def __str__(self) -> str:
        return str(self.assessment_id) + " : " + str(self.question_id)


class UserQuestionnaire(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    assessment_id = models.ForeignKey(Assessment, on_delete=models.DO_NOTHING)
    question_id = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING)
    answer = models.JSONField()  # ArrayField in case of any issue
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        unique_together = (('user_id', 'assessment_id', 'question_id'),)


class UserAssessment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    assessment_id = models.ForeignKey(Assessment, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=100, default="COMPLETED")
    score = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        unique_together = (('user_id', 'assessment_id'),)
