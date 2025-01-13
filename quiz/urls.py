# myapp/urls.py
from rest_framework.routers import DefaultRouter
from .views import QuizQuestionViewSet
from .views import QuizViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include

router = DefaultRouter()
router.register(r'quiz-questions', QuizQuestionViewSet)
router.register(r'quizzes', QuizViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="API documentation for my Django project",
      contact=openapi.Contact(email="contact@myapi.com"),
   ),
   public=True,
)


urlpatterns = [
    path('', include(router.urls)), 
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-schema'),
]