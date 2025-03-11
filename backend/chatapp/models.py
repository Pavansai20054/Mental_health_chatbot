from django.db import models

class MoodLog(models.Model):
    user_message = models.TextField()
    chatbot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_message} | Bot: {self.chatbot_response}"
