from django.db import models


class CorporateUser(models.Model):
    name = models.CharField(max_length=50, blank=False)


class User(models.Model):
    user_choices = (('NORMAL', 'NORMAL'), ('CORPORATE', 'CORPORATE'))
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=500)
    is_email_verified = models.BooleanField(default=False)
    phone_number = models.PositiveBigIntegerField(null=True)
    is_phone_verified = models.BooleanField(default=False)
    year_of_experience = models.FloatField(default=0)
    resume = models.CharField(max_length=100, default='')
    department = models.CharField(max_length=100, default='')
    designation = models.CharField(max_length=100, default='')
    user_type = models.CharField(max_length=100, choices=user_choices)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    corporate_id = models.ForeignKey(CorporateUser, on_delete=models.DO_NOTHING)
    # last_login = models.DateTimeField()
    #
    # def get_full_name(self):
    #     if self.last_name:
    #         return f"{self.first_name} {self.last_name}"
    #     else:
    #         return self.first_name
    #
    # def get_short_name(self):
    #     return self.first_name
    #
    # def get_first_name(self):
    #     return self.first_name
    #
    # def get_last_name(self):
    #     return self.last_name


class Assessment(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    duration = models.IntegerField()  # Save time in minutes
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # OR CASCADE
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Questionnaire(models.Model):
    name = models.CharField(max_length=255)
    options = models.JSONField()  # ArrayField in case of any issue
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class AssessmentQuestionnaire(models.Model):
    assessment_id = models.ForeignKey(Assessment, on_delete=models.DO_NOTHING)
    question_id = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (('assessment_id', 'question_id'),)


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
