from django.db import models

from make.models import Make

class Group(models.Model)
    group_name = models.CharField(max_length = 50)
    member_name = models.ForeignKey(Make.first_name + " " Make.last_name)
    member_phone_number = models.ForeignKey(Make.phone_number)
    member_email = models.ForeignKey(Make.email)
    birthday = models.DateField()
    
    def __unicode__(self):
        return self.group_name
