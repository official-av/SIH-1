from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Department(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department_name = models.CharField(max_length=500)

    def __str__(self):
        return "Name : {}".format(self.department_name)


class Question(models.Model):
    text = models.CharField(max_length=5000)
    subject = models.CharField(max_length=2000)
    type = models.CharField(max_length=500)
    timestamp = models.DateField()
    asked_by = models.ForeignKey(User)
    is_recommended = models.BooleanField(default=False)

    @staticmethod
    def deadline_check(self):
        pass

    def __str__(self):
        return "{} | {}".format(self.subject, self.text)


class QuestionFor(models.Model):
    question = models.ForeignKey(Question)
    asked_to = models.ForeignKey(Department)
    answer = models.TextField(null=True)


    def __str__(self):
        return "{}".format(self.question.subject,self.asked_to.department_name)


class Recommendation(models.Model):
    question = models.ForeignKey(Question)
    to = models.ForeignKey(Department,related_name='recommeded_to_me')
    by = models.ForeignKey(Department,related_name='recommeded_by_me')
    recommeded_answer = models.TextField(max_length=5000)

    def __str__(self):
        return "{} | {} | {}".format(self.question.subject,self.recommeded_answer,self.to.department_name)

