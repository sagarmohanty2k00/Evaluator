from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20)
    fullMarks = models.IntegerField(default=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    totalQuestions = models.IntegerField(default=1)
    toBeAnswered = models.IntegerField(default=1)

    def __str__(self):
        return (str(self.subject) + " - " + str(int(self.marks) * int(self.toBeAnswered)))