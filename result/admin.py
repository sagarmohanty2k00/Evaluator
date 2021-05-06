from django.contrib import admin
from .models import Question, Subject

# Register your models here.
admin.site.register(Subject)
admin.site.register(Question)