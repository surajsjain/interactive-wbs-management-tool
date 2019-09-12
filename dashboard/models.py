from django.db import models
from django.contrib.auth.models import User

import datetime


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+2)]

def current_year():
    return datetime.date.today().year



# Create your models here.

class CostCenters(models.Model):
    cc_id = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.cc_id+' - '+self.name

class Budget(models.Model):
    year = models.IntegerField(('year'), choices=year_choices(), default=current_year())
    quarter = models.IntegerField(('quarter'), choices=[(1, 1),  (2, 2), (3, 3), (4, 4)])
    type = models.CharField(('type'), choices=[('Before Quarter', 'Before Quarter'), ('During Quarter', 'During Quarter')], max_length=30)
    product = models.CharField(max_length=200)

    def __str__(self):
        return str(self.year)+' - '+self.product+' - '+self.type

class WBS(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    # cc_index = models.CharField(max_length=20)
    # name = models.CharField(max_length=200) ##TV Ads, Newspaper Islands

    cc = models.ForeignKey(CostCenters, on_delete=models.CASCADE, default=None)
    amount = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.budget.product +' - '+ self.cc.name

class Transfer(models.Model):
    wbs_item = models.ForeignKey(WBS, on_delete=models.CASCADE, related_name='wbs_item')
    type = models.IntegerField() # 1- add, 2- remove, 3- Transfer from another wbs
    timeInitiated = models.DateTimeField(default=datetime.datetime.now())

    amount = models.DecimalField(decimal_places=2, max_digits=8)
    transfer_target = models.ForeignKey(WBS, on_delete=models.CASCADE, blank=True, related_name='transfer_target')

    status = models.BooleanField(default=True)

    # def __str__(self):
    #     return str(self.wbs_item.budget.product)+' - '+str(self.wbs_item.cc.name)+' - '+str(self.amount)

class Comment(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wbs_item = models.ForeignKey(WBS, on_delete=models.CASCADE)
    text = models.CharField(max_length=3000, blank=True)
    attachment = models.FileField(upload_to='attachments/%Y/%m/%d/', blank=True)

    def __str__(self):
        return str(self.timestamp)+' - '+self.user.username
