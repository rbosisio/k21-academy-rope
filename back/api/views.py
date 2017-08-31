from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.	
class ApiDreams(APIView):

	renderer_classes = (JSONRenderer, )

	def get(self,request):
		return Response({'msg': 'works'})
