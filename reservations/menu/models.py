from django.db import models

class Menu(models.Model):
    category = models.CharField(max_length = 100)
    name = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.CharField(max_length = 500)
    special_instructions = models.CharField(max_length = 500)
    
    def __unicode__(self):
        return self.name
