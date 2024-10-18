from django.contrib import admin
from .models import QuizQuestion
from .models import Capital
from .models import Feedback
from .models import Quiz

# Register the model
admin.site.register(QuizQuestion)
admin.site.register(Quiz)
admin.site.register(Capital)
admin.site.register(Feedback)