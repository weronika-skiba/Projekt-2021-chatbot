from django.contrib import admin
from .models import Question
from .models import Answer
from .models import SubmitCount

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(SubmitCount)