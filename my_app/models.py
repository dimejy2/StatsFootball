from django.db import models

# Create your models here.
class Currency(models.Model):
    identifier = models.CharField(max_length=3) #USD,EUR etc.
    long_name = models.CharField(max_length=50) #United States Dollar etc.
    date_added = models.DateTimeField() #When added to database
    def __str__(self):
        return self.identifier + " " + self.long_name

class Rates(models.Model):
    id_1 = models.ForeignKey(Currency) #A link to a Currency object
    id_2 = models.CharField(max_length=3) #Identifier for currency 2
    rate = models.FloatField(default=1.0) #exchange rate
    last_update_time = models.DateTimeField() #last time updated

    def __str__(self):
        return self.id_1.identifier + " " + self.id_2 + " " + str(self.rate)

    def time_since_last_update(self):
        from datetime import datetime,timezone
        now=datetime.now(timezone.utc)
        try:
            time_diff = now - self.last_update_time
        except:
            return "Never"
        return time_diff

from django.contrib.auth.models import User

class Investor(models.Model):
    user=models.OneToOneField(User)
    account_number=models.CharField(max_length=10)

    def __str__(self):
        return "Investor: " + str(self.user.username)

class Balances(models.Model):
    account_holder = models.ForeignKey(Investor)
    currency_id = models.CharField(max_length=3)
    value = models.FloatField(default=0.0)


### Step 1 - create your player model ###
class Player(models.Model):
    name = models.CharField(max_length=30)
    pos = models.CharField(max_length=30)
    stat1 = models.FloatField(null=True)
    stat2 = models.FloatField(null=True)
    stat3 = models.FloatField(null=True)
    stat4 = models.FloatField(null=True)
    stat5 = models.FloatField(null=True)
    stat6 = models.FloatField(null=True)
    stat7 = models.FloatField(null=True)
    stat8 = models.FloatField(null=True)
    #stat1 = models.CharField(max_length=30, blank=True, null=False)
    #stat2 = models.CharField(max_length=30, blank=True, null=False)
    #stat3 = models.CharField(max_length=30, blank=True, null=False)
    #stat4 = models.CharField(max_length=30, blank=True, null=False)
    #stat5 = models.CharField(max_length=30, blank=True, null=False)
    #stat6 = models.CharField(max_length=30, blank=True, null=False)
    #stat7 = models.CharField(max_length=30, blank=True, null=False)
    #stat8 = models.CharField(max_length=30, blank=True, null=False)
    def __str__(self):
        return self.name
