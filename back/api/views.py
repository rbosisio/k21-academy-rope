from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models import Dream, Volunteer, AvailableDaysTimes
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
		dream = None
		try:
			dream = Dream(
					dreamer_name = body['dreamer_name'],
					dreamer_age = body['dreamer_age'],
					dreamer_address = body['dreamer_address'],
					dreamer_health_conditions = body['dreamer_health_conditions'],
					contact_name = body['contact_name'],
					contact_email = body['contact_email'],
					contact_phone = body['contact_phone'],
					contact_liason = body['contact_liason'],
					inmate = body['inmate'],
					local = body['local'],
					local_address = body['local_address'],
					local_name = body['local_name'],
					local_phone = body['local_phone'],
					medical_approved = body['medical_approved'],
					parental_approved = body['parental_approved'],
					description = body['description'],
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
			response = serializers.serialize("json",[Volunteer.objects.get(pk=id),])
		else:
			response = serializers.serialize("json",Volunteer.objects.all())
		return Response(json.loads(response))

	def post(self,request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		volunteer = None
		try:
			volunteer = Volunteer(
					name = body['name'],
					nickname = body['nickname'],
					birthdate = body['birthdate'],
					telephone = body['telephone'],
					cellphone = body['cellphone'],
					email = body['email'],
					address = body['address'],
					personal_characteristics = body['personal_characteristics'],
					talents = body['talents'],
					assignment = body['assignment'],
					status = body['status']
				)
			days_times = body['available_days_times']
			volunteer.save()
			for day_time in days_times:
				print(day_time)
				day = day_time.split('-')[0]
				time = day_time.split('-')[1]
				model_day_time = AvailableDaysTimes.objects.get(day=day, time=time)
				volunteer.available_days_times.add(model_day_time)
			volunteer.save()
		except Exception as e:
			return Response({'error': True, 'msg': 'Erro ao salvar o voluntário!', "exception": str(e)}, status=status.HTTP_400_BAD_REQUEST)
		volunteer_json = json.loads(serializers.serialize("json", [Volunteer.objects.get(pk=volunteer.pk),]))
		return Response(volunteer_json)