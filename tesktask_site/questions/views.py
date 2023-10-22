from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
import requests
import json
from questions.models import Questions


class QuestionsAPIView(APIView):
   def post(self,request):
      count=request.GET
      table_count=Questions.objects.count()
      data = get_data_from_api('https://jservice.io/api/random?',count)
      read_json(data)
      f = Questions.objects.last()
      a=count.get('count')
      b=int(a)
      if table_count==0 and b==1:
         data=table_none()
      elif b>1:
         s=f.pk - 1
         dat=Questions.objects.get(pk=s)
         data = encode(dat)

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
      save_data(answer)
   return answer
def save_data(data):
   obj, created = Questions.objects.get_or_create(
      id_questions=data['id_questions'],
      text=data['text'],
      answer=data['answer'],
      time_create=data['time_create']
   )
   if not created:
      data=get_data_from_api('https://jservice.io/api/random?', 1)
      read_json(data)

def encode(data):

   date = data.time_create.strftime("%Y-%m-%d %H:%M:%S")

   Json= json.dumps({'id_questions':data.id_questions,
                     'text':data.text,
                     'answer':data.answer,
                     'time_create':date})
   return Json

def table_none():
   Json = json.dumps({'id_questions': '',
                      'text': '',
                      'answer': '',
                      'time_create': ''})

   return Json