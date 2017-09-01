from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models import Dream
import json
from django.core import serializers

# Create your views here.

class ApiDreams(APIView):

	renderer_classes = (JSONRenderer, )

	def get(self,request, id=None):
		if id:
			response = serializers.serialize("json",[Dream.objects.get(pk=id),])
		else:
			response = serializers.serialize("json",Dream.objects.all())
		return Response(json.loads(response))

	def post(self,request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		try:
			dream = Dream(
					name=body['name'],
					age=body['age'],
					email=body['email'],
					address=body['address'],
					phone=body['phone'],
					inmate=body['inmate'],
					hospital_name=body['hospital_name'],
					hospital_contact=body['hospital_contact'],
					medical_approved=body['medical_approved'],
					parental_approved=body['parental_approved'],
					description=body['description'],
					hospital_address=body['hospital_address'],
					observation=body['observation'],
					liason=body['liason'],
					status=body['status'],
					planning_description=body['planning_description'],
					health_conditions=body['health_conditions'],
					contact_name=body['contact_name'],
					dream_report=body['dream_report']
				)
			dream.save()
		except Exception as e:
			return Response({'error': True, 'msg': 'Erro ao salvar o sonho!', 'field': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		dream_json = json.loads(serializers.serialize("json", [dream,]))
		return Response(dream_json)



# =================================================================================================== #



class ApiVolunteers(APIView):

	renderer_classes = (JSONRenderer, )

	def get(self,request, id=None):
		if id:
			response = serializers.serialize("json",[Dream.objects.get(pk=id),])
		else:
			response = serializers.serialize("json",Dream.objects.all())
		return Response(json.loads(response))

	def post(self,request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		try:
			dream = Dream(
					name=body['name'],
					age=body['age'],
					email=body['email'],
					address=body['address'],
					phone=body['phone'],
					inmate=body['inmate'],
					hospital_name=body['hospital_name'],
					hospital_contact=body['hospital_contact'],
					medical_approved=body['medical_approved'],
					parental_approved=body['parental_approved'],
					description=body['description'],
					hospital_address=body['hospital_address'],
					observation=body['observation'],
					liason=body['liason'],
					status=body['status'],
					planning_description=body['planning_description'],
					health_conditions=body['health_conditions'],
					contact_name=body['contact_name'],
					dream_report=body['dream_report']
				)
			dream.save()
		except Exception as e:
			return Response({'error': True, 'msg': 'Erro ao salvar o sonho!'}, status=status.HTTP_400_BAD_REQUEST)
		dream_json = json.loads(serializers.serialize("json", [dream,]))
		return Response(dream_json)