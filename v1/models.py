from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    authority = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class program(models.Model):
    region = models.TextField()

    program_name = models.CharField(max_length=50)  # 프로그램명
    register_date = models.DateTimeField(default=timezone.now)  # 등록일

    community_centre = models.TextField()  # 주민센터
    # weekly = models.CharField(max_length=50)  # . 으로 분할함 (주마다 하는 프로그램)
    number_of_recruitment = models.IntegerField()  # 모집인원
    training_period_Start = models.TextField()  # 교육 시작일
    training_period_End = models.TextField()  # 교육 마감일
    receipt_period_Start = models.TextField()  # 접수 시작일
    receipt_period_End = models.TextField()  # 접수 마감일

    teacher = models.TextField()  # 강사명
    contact = models.TextField()  # 연락처

    detail = models.TextField()  # 프로그램 소개

    def __str__(self):
        return self.program_name



#
# class user(models.Model):
#
