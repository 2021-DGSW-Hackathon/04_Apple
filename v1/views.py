from django.shortcuts import render
from django.core import serializers
from django.views import View
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import *

import json

from django.views.decorators.csrf import csrf_exempt    # csrf 비활성화 라이브러리
from django.utils.decorators import method_decorator    # csrf 비활성화를 위한 메서드, 클래스 데코레이터
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.serializers import serialize


@method_decorator(csrf_exempt, name='dispatch')         # csrf 비활성화
class programInfo(View):
    def get(self, request):
        programs = program.objects.all().order_by('-id')

@method_decorator(csrf_exempt, name='dispatch')
class signUp(APIView):
    def post(self, request):
        try:
            user = User.objects.create_user(
                username=request.data['id'],
                password=request.data['password'],
            )
            profile = Profile(
                user=user,
                authority=request.data['authority'],
                birth=request.data['birth'],
                name=request.data['name'],
            )

            user.save()
            profile.save()

            token = Token.objects.create(user=user)
            return Response({
                "status": 200,
                "data":{
                    "token": token.key
                }
            })
        except:
            return JsonResponse({
                "status": 400,
                "data": {
                    "token": ""
                }
            })


@method_decorator(csrf_exempt, name='dispatch')
class logIn(APIView):
    def post(self, request):
        try:
            user = authenticate(username=request.data['id'], password=request.data['password'])
            if user is not None:
                token = Token.objects.get(user=user)
                return Response({
                    "status": 200,
                    "data": {
                        "token": token.key
                    }
                })
            else:
                return Response({
                    "status": 400,
                    "data": {
                        "token": ""
                    }
                })
        except:
            return Response({
                "status": 400,
                "data": {
                    "token": ""
                }
            })


@method_decorator(csrf_exempt, name='dispatch')
class checkToken(APIView):
    def post(self, request):
        try:
            user = request.user
            user = user.profile.authority
            print(request.auth)
            return JsonResponse({
                "status": 200,
                "data": {
                    "isItVaild": True
                }
            })
        except:
            return JsonResponse({
                "status": 410,
                "data": {
                    "isItVaild": False
                }
            })




@method_decorator(csrf_exempt, name='dispatch')
class programs(View):
    def get(self, request):
        try:
            try:
                sort = request.data['sort_by']
            except:
                programs = program.objects.all().order_by('-id')
                programs = json.loads(serialize('json', programs))
                return JsonResponse({
                    "status": 200,
                    "data": programs
                })
            if sort == 'Old':
                programs = program.objects.all().order_by('id')
                programs = json.loads(serialize('json', programs))
                return JsonResponse(programs)
            else:
                programs = program.objects.all().order_by('-id')
                if not programs:
                    return JsonResponse({
                        "status": 400,
                        "data": []
                    })
                programs = json.loads(serialize('json', programs))
                return JsonResponse({
                    "status": 200,
                    "data": programs
                })
        except:
            return JsonResponse({
                "status": 400,
                "data": []
            })

@method_decorator(csrf_exempt, name='dispatch')
class programs_make(APIView):
    def post(self, request):
        print(request.user)
        print(request.META.get('HTTP_AUTHORIZATION'))
        user = request.user
        user_auth = user.profile.authority
        if user_auth == 'employee':
            Program = program(
                program_name=request.data['program_name'],
                community_centre=request.data['community_centre'],
                number_of_recruitment=request.data['number_of_recruitment'],
                training_period_Start=request.data['training_period_Start'],
                teacher=request.data['teacher'],
                contact=request.data['contact'],
                detail=request.data['detail'],
                receipt_period_Start=request.data['receipt_period_Start'],
                receipt_period_End=request.data['receipt_period_End'],
                region=request.data['region']
            )
            Program.save()
            return JsonResponse({
                "status": 200
            })
        else:
            return JsonResponse({
                "status": 403
            })

@method_decorator(csrf_exempt, name='dispatch')
class programs_delete(APIView):
    def delete(self, request):
        user = request.user
        user_auth = user.profile.authority
        if user_auth == 'employee':
            index = request.data['index']
            Program = program.objects.get(pk=index)
            Program.delete()
            return JsonResponse({
                "status": 200
            })
        else:
            return JsonResponse({
                "status": 403
            })

@method_decorator(csrf_exempt, name='dispatch')
class programs_modify(APIView):
    def put(self, request):
        print("OK")
        user = request.user
        user_auth = user.profile.authority
        if user_auth == 'employee':
            index = request.data['index']
            Program = program.objects.get(pk=index)
            program_name = request.data['program_name']
            community_centre = request.data['community_centre']
            number_of_recruitment = request.data['number_of_recruitment']
            training_period_Start = request.data['training_period_Start']
            training_period_End = request.data['training_period_End']
            teacher = request.data['teacher']
            contact = request.data['contact']
            detail = request.data['detail']
            receipt_period_Start = request.data['receipt_period_Start']
            receipt_period_End = request.data['receipt_period_End']
            region = request.data['region']

            if program_name:
                Program.program_name = program_name
            if community_centre:
                Program.community_centre = community_centre
            if number_of_recruitment:
                Program.number_of_recruitment = number_of_recruitment
            if training_period_Start:
                Program.training_period_Start = training_period_Start
            if training_period_End:
                Program.training_period_End = training_period_End
            if teacher:
                Program.teacher = teacher
            if contact:
                Program.contact = contact
            if detail:
                Program.detail = detail
            if receipt_period_Start:
                Program.receipt_period_Start = receipt_period_Start
            if receipt_period_End:
                Program.receipt_period_End = receipt_period_End
            if region:
                Program.region = region

            Program.save()


