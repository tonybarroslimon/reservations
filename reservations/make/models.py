from django.db import models

class Make(models.Model):
    first_name = models.Charfield(max_length = 150)
    last_name = models.Charfield(max_length = 150)
    special_requests = models.Charfield(max_length = 500)
    date = models.DateAndTimeField(auto_now_update)
    email = models.EmailField()
    phone_number = models.IntField(max_length = 10)
    
    
class Details(models.Model):
    name = models.Charfield(max_length = 150)
    available_spots = models.Intfield()
    time_slots = models.Intfield()
    
    #code

