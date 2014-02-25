from django.db import models

class Calendar(models.Model):
    event_name = models.CharField(max_length = 150)
    special_notes = models.CharField(max_length = 150)
    event_date = models.DateTimeField('Event Date')
    
    def __unicode__(self):
        return self.event_name
    
