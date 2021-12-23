import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.




class reminder():
    Time = models.CharField(max_length=200) #### fix this datatype later


class Patient():
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    reminders = models.ForeignKey(reminder, on_delete=models.CASCADE) ## Right now this is an error. 




class User(models.Model):
    clearance = models.IntegerField(default=0) ### needs to be maped per patient
    patients = models.ForeignKey(Patient, on_delete=models.CASCADE) ## Right now this is an error. 
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)





class Question(models.Model):
    question_text = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    picture = models.CharField(max_length=200) #File path
    a1 = models.CharField(max_length=200)
    a2 = models.CharField(max_length=200)
    a3 = models.CharField(max_length=200)
    a4 = models.CharField(max_length=200)
    answer = models.IntegerField(default=0) 
    lastSubAnswer = models.IntegerField(default=0) 


class results():
    ## relation between a quize and its compleation time. 
    ## stored quize
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    numCorrect = models.IntegerField(default=0) 
    totalQuestions = models.IntegerField(default=0) 
    pass

class Quiz(models.Model):
    # array of questions
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    pass 
