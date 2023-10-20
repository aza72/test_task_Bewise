#from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
import requests

from questions.models import Questions


class QuestionsAPIView(APIView):
   def post(self,request):
      count=request.GET
      data = get_data_from_api('https://jservice.io/api/random?',count)
      answer = read_json(data)
      save_data(answer)
      #print (answer)
      return Response(data)


def get_data_from_api(url,count):
   response = requests.get(url, params=count)
   data = response.json()
   return data

def read_json(data):
   for d in data:
      answer={
         'id_questions' : d['id'],
         'text' : d['question'],
         'answer' : d['answer'],
         'time_create': d['created_at']
      }
   return answer
def save_data(data):

   Questions.objects.create(
      id_questions=data['id_questions'],
      text=data['text'],
      answer=data['answer'],
      time_create=data['time_create']
   )
