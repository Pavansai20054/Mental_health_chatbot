import requests
import json
import logging
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatapp.models import MoodLog
from chatapp.serializers import MoodLogSerializer
from django.views.decorators.csrf import csrf_exempt

# Set up logging
logger = logging.getLogger(__name__)

# Gemini API Key
GENAI_API_KEY = "AIzaSyA_g4e3DxYJTsO44BjzA6jTeJa0KmKDA8o"  # SECURITY WARNING: Move this to an environment variable

@api_view(['GET'])
def get_mood_logs(request):
    logs = MoodLog.objects.all()
    return Response(MoodLogSerializer(logs, many=True).data)

def home(request):
    return render(request, 'home.html')

def chatbot_view(request):
    chat_type = request.GET.get('type')
    if chat_type not in ['student', 'professional']:
        return JsonResponse({"error": "Invalid type. Use 'student' or 'professional'."}, status=400)
    return render(request, 'chatbot.html', {'type': chat_type})

def chat(request):
    return render(request, 'chat.html')

def mood_tracking(request):
    return render(request, 'mood_tracking.html')

def emergency_support(request):
    return render(request, 'emergency_support.html')

def stress_management(request):
    return render(request, 'stress_management.html')

@csrf_exempt
@api_view(['POST'])
def get_chatbot_response(request):
    user_message = request.data.get('message', '').strip()
    if not user_message:
        return JsonResponse({"error": "No message provided"}, status=400)
    
    try:
        response = get_gemini_response(user_message)
        MoodLog.objects.create(user_message=user_message, chatbot_response=response)
        return JsonResponse({"response": response, "source": "bot"})
    except Exception as e:
        logger.error(f"Chatbot response error: {e}")
        return JsonResponse({"error": "An error occurred. Try again later."}, status=500)

def get_gemini_response(user_message):
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GENAI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": user_message}]}]}
    
    try:
        response = requests.post(api_url, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        response_json = response.json()
        
        candidates = response_json.get("candidates", [])
        if candidates:
            return candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        return ""
    except requests.exceptions.RequestException as e:
        logger.error(f"Gemini API request failed: {e}")
        return ""