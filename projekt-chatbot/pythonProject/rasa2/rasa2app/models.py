from django.db import models


class SubmitCount(models.Model):
    s_count = models.IntegerField()

    def ret_int(self):
        return self.s_count


class Question(models.Model):
    q_text = models.CharField(max_length=250)
    q_date = models.DateTimeField().auto_now

    def ret_string(self):
        return self.q_text


class Answer(models.Model):
    a_text = models.CharField(max_length=250)
    a_date = models.DateTimeField().auto_now

    def ret_string(self):
        return self.a_text
