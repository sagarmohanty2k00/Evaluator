from django.db import models
from student.models import Student
from result.models import Subject, Question

# Create your models here.

class MarksAwarded(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    marksAwarded = models.IntegerField(default=0)

    def __str__(self):
        return  self.marksAwarded

