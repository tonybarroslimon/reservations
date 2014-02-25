from django.db import models

from make.models import Make

class Rewards(models.Model):
    reward_number = models.ForeignKey(Make.phone_number)
    reward_email = models.ForeignKey(Make.email)
    reward_points = models.IntegerField(default = 0)
    receipt_number = models.IntegerField(max_length = 30)
