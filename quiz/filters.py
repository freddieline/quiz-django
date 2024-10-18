import django_filters
from .models import QuizQuestion

class QuizQuestionFilter(django_filters.FilterSet):
    quiz_name = django_filters.CharFilter(field_name='quiz__name', lookup_expr='icontains')  # Case-insensitive match

    class Meta:
        model = QuizQuestion
        fields = [] 