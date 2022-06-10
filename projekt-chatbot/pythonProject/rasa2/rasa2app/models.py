from django.db import models


class SessionCount(models.Model):
    s_count = models.IntegerField()

    def ret_int(self):
        return self.s_count


class SessionText(models.Model):
    s_text = models.CharField(max_length=250)
    s_type = models.CharField(max_length=1)
    s_id = models.IntegerField()
    s_key = models.CharField(max_length=32)

    def ret_string(self):
        return self.s_text

    def ret_char(self):
        return self.s_type

    def ret_id(self):
        return self.s_id

    def ret_key(self):
        return self.s_key


class Question(models.Model):
    q_text = models.CharField(max_length=250)

    def ret_string(self):
        return self.q_text
