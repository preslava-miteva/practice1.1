from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import Score
import json
from django.views.decorators.csrf import csrf_exempt

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['username', 'gameID', 'scoreValue']

@api_view(['POST'])
@csrf_exempt
def postFunc(request):
    if request.method != 'POST':
        return JsonResponse("Not allowed", status = 405)
    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse("Error", status = 400)

    sV = data.get('scoreValue')
    if sV is None:
        return JsonResponse({"error": "scoreValue is required"}, status = 400)
    if not isinstance(sV, int) or sV <= 0:
        return JsonResponse({"error": "scoreValue must be a positive integer"}, status=400)

    serializer = ScoreSerializer(data = data)
    if not serializer.is_valid():
        return JsonResponse(serializer.errors, status = 400)
    newScore = serializer.save()
    return JsonResponse(serializer.data, status=201)


