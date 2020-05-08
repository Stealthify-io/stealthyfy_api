from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from utils.script import get_distance
from utils.stores import get_places
from core.models import User

from rest_framework import viewsets

from core.models import User
from core.serializers import UserSerializer

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)
from rest_framework.response import Response
import json;


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

@csrf_exempt
def distance(request):
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed"})

    if "lat" not in request.POST or "lng" not in request.POST:
        return JsonResponse({"message": "Please provide lat and lng value"})

    lat = request.POST.get("lat")
    lng = request.POST.get("lng")

    d = get_distance(float(lat), float(lng))

    return JsonResponse({
        "message": "success",
        "distance": "{:.2f}".format(d)
    })


@csrf_exempt
def places(request):
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed"})

    if "lat" not in request.POST or "lng" not in request.POST:
        return JsonResponse({"message": "Please provide lat and lng value"})

    lat = request.POST.get("lat")
    lng = request.POST.get("lng")

    d = get_places(float(lat), float(lng))

    return JsonResponse({
        "message": "success",
        "results": d
    })

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return JsonResponse({'success':False,'message': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(is_superuser=False,email=email, password=password)
    if not user:
        return JsonResponse({'success':False,'message': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)

    return JsonResponse({'message':'Success','success':True,'token': token.key,'user':{"first_name":user.first_name,"last_name":user.last_name,"email":user.email}},
                    status=HTTP_200_OK)