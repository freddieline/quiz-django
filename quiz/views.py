# myapp/views.py
from rest_framework import viewsets
from .models import QuizQuestion
from .models import Quiz
from django.db.models import F
from .serializers import QuizQuestionSerializer
from .serializers import QuizSerializer
from .filters import QuizQuestionFilter
from django_filters.rest_framework import DjangoFilterBackend

class QuizQuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete'] 
    filterset_class = QuizQuestionFilter

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']  # Allows both PUT and PATCH