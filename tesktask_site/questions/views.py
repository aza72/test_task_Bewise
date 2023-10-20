from django.contrib.sites import requests
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
      response = get_data_from_api('https://jservice.io/api/random?',count)
      #Questions.objects.create(id_questions=response.list['answer'])
      #json_to_obj = json.loads(response)

      return Response(response)


def get_data_from_api(url,count):
   response = requests.get(url, params=count)
   data = response.json()
   return data


# def save_data_to_model(data):
#    item = Questions(id_questions=data['id'])
#    item.save()