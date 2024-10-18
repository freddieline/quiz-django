# myapp/urls.py
from rest_framework.routers import DefaultRouter
from .views import QuizQuestionViewSet
from .views import QuizViewSet

router = DefaultRouter()
router.register(r'quiz-questions', QuizQuestionViewSet)
router.register(r'quizzes', QuizViewSet)

urlpatterns = router.urls