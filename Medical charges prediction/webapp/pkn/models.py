from django.db import models

# Create your models here.
class register_new(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    mail_id = models.EmailField()
    password = models.CharField(max_length=16)
    confirm_password = models.CharField(max_length=16)

class login_new(models.Model):
    email_id = models.EmailField()
    password2 = models.CharField(max_length=16)

class contacting_new(models.Model):
    contact_name = models.CharField(max_length=40)
    contact_mail = models.EmailField(max_length=40)
    country = models.CharField(max_length=40)
    subject = models.CharField(max_length=200)

class predict(models.Model):
    # predict_name = models.CharField(max_length=40)
    # predict_mail = models.EmailField(max_length=40)
    age = models.CharField(max_length=4)
    sex = models.CharField(max_length=7)
    bmi = models.CharField(max_length=10)
    children = models.CharField(max_length=2)
    smoker = models.CharField(max_length=4)
    region = models.CharField(max_length=13)
    # charges = models.CharField(max_length=10)

class collect_new(models.Model):
    predict_name = models.CharField(max_length=40)
    predict_mail = models.EmailField(max_length=40)
    age = models.CharField(max_length=4)
    sex = models.CharField(max_length=7)
    bmi = models.CharField(max_length=10)
    children = models.CharField(max_length=2)
    smoker = models.CharField(max_length=4)
    region = models.CharField(max_length=13)
    # charges = models.CharField(max_length=10)

