from django.db import models

from menu.models import Menu
from contacts.models import Group

class Order(models.Model):
    class Meta:
        first_name = Group.first_name
        last_name = Group.last_name
        cart = Menu.name
        total = Menu.price
        special_instructions = Menu.special_instructions
    
    def __unicode__(self):
        return self.last_name
    


