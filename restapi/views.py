from django.shortcuts import render
from rest_framework import viewsets
from .disable_csrf import QuizSerializer, QuestionsSerializer
from .models import quiz, questions
# Create your views here.

def error_404_view(request,exception):
    return render(request,'{}')

class QuizViewSet(viewsets.ModelViewSet):
    queryset = quiz.objects.all().order_by('name')
    serializer_class = QuizSerializer

    
class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = questions.objects.all().order_by('name')
    serializer_class = QuestionsSerializer
