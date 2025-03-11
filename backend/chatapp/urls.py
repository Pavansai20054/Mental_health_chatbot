# chatapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Home page route
    path('', views.home, name='home'),

    # Chatbot view route
    path('chatbot/', views.chatbot_view, name='chatbot_view'),

    # Chat page route
    path('chat/', views.chat, name='chat'),

    # Emergency support route
    path('emergency_support/', views.emergency_support, name='emergency_support'),

    # API endpoint for chatbot interaction (POST)
    path('api/chat/', views.get_chatbot_response, name='get_chatbot_response'),

    # API endpoint for mood logs (GET)
    path('api/mood_logs/', views.get_mood_logs, name='get_mood_logs'),

    # Mood tracking route
    path('mood_tracking/', views.mood_tracking, name='mood_tracking'),

    # Stress management route
    path('stress_management/', views.stress_management, name='stress_management'),
]
