from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from azjwt.django.rest_framework import MyAuthentication

class HelloViewSet(ViewSet):
    authentication_classes = [MyAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response("Hi there!")
