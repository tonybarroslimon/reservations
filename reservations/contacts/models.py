from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    member_phone_number = models.IntegerField(max_length = 10)
    member_email = models.CharField(max_length = 300)
    birthday = models.DateField()
    
    def __unicode__(self):
        return self.group_name
