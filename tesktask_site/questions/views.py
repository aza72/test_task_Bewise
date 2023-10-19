from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.views import APIView


class QuestionsAPIView(APIView):
    def get(self, request):
        response = requests.get('https://jservice.io/api/random?count=1')
        data = response.json()
        print(data)
        return data
    def post(self,request):
        data = self.get()
        print(data)
        return data