# myapp/views.py
from rest_framework import viewsets
from .models import QuizQuestion
from .models import Quiz
from django.db.models import F
from .serializers import QuizQuestionSerializer
from .serializers import QuizSerializer
from .filters import QuizQuestionFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError

class QuizQuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete'] 
    filterset_class = QuizQuestionFilter

    def create(self, request, *args, **kwargs):
        if not request.data:
            raise ValidationError("Request body cannot be empty.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.data:
            raise ValidationError("Request body cannot be empty.")
        return super().update(request, *args, **kwargs)

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']  # Allows both PUT and PATCH

    def create(self, request, *args, **kwargs):
        if not request.data:
            raise ValidationError("Request body cannot be empty.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.data:
            raise ValidationError("Request body cannot be empty.")
        return super().update(request, *args, **kwargs)