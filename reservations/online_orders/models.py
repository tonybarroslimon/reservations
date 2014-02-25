from django.db import models

from menu.models import Menu
from contacts.models import Group

class Order(models.Model):
    name = models.ForeignKey(Group.member_name)
    cart = models.ForeignKey(Menu.name)
    total = models.ForeignKey(Menu.price)
    special_instructions = models.ForeignKey(Menu.special_instructions)
    
    def __unicode__(self):
        return self.name
    


