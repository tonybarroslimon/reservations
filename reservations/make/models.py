from django.db import models

class Make(models.Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    special_requests = models.CharField(max_length = 500)
    reservation_date = models.DateTimeField()
    reservation_made = models.DateTimeField(auto_now_add = True)
    email = models.CharField(max_length = 300)
    phone_number = models.IntegerField(max_length = 10)
    
    def __unicode__(self):
        return self.last_name
    
    
class Details(models.Model):
    restaurant_name = models.CharField(max_length = 150)
    details = models.ForeignKey(Make)
    available_spots = models.TimeField()
    time_slots = models.IntegerField(max_length = 100)
    
    def __unicode__(self):
        return self.restaurant_name
    
    

