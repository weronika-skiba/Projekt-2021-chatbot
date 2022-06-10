from django.contrib import admin
from .models import Question
from .models import SessionText
from .models import SessionCount


admin.site.register(Question)
admin.site.register(SessionText)
admin.site.register(SessionCount)