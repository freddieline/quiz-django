from django.db import models

class Continent(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically uses a sequence for the ID
    name = models.CharField(max_length=255, unique=True)
    class Meta:
        managed = False
        db_table = 'continents'
    def __str__(self):
        return self.name


class Quiz(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically uses a sequence for the ID
    name = models.CharField(max_length=100)
    class Meta:
        managed = False 
        db_table = 'quizzes'
    def __str__(self):
        return self.name

  
class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    class Meta:
        db_table = 'feedback'

    def __str__(self):
        return self.feedback

class DifficultyLevel(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically uses a sequence for the ID
    name = models.CharField(max_length=50)

    class Meta:
        managed = False 
        db_table = 'difficulty_levels'

    def __str__(self):
        return self.name


class Capital(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically uses a sequence for the ID
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255, unique=True)
    continent = models.ForeignKey(Continent, null=True, blank=True, on_delete=models.SET_NULL)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'country')  # Adding a unique constraint for (name, country)
        managed = False 
        db_table = 'capitals'

    def __str__(self):
        return self.name


class QuizQuestion(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically uses a sequence for the ID
    question = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255, null=True, blank=True)
    answer_3 = models.CharField(max_length=255, null=True, blank=True)
    answer_4 = models.CharField(max_length=255, null=True, blank=True)
    correct_answer = models.IntegerField()
    difficulty_level = models.ForeignKey(DifficultyLevel, null=True, blank=True, on_delete=models.SET_NULL)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    additional_info = models.TextField(null=True, blank=True)
    
    class Meta:
        managed = False 
        db_table = 'quiz_questions'

    def __str__(self):
        return self.question
    
    @property
    def quiz_name(self):
        return self.quiz.name