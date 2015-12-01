from django.contrib import admin

# Register your models here.
from my_app.models import Currency,Rates

class RatesInline(admin.TabularInline): #or StackedInline
    model = Rates #The model connected
    readonly_fields = ('time_since_last_update',)
    extra = 3 #enough space for three extra Rates

class CurrencyAdmin(admin.ModelAdmin):
    fields = ['identifier','long_name','date_added']
    inlines=[RatesInline] #Connection to Rates
    list_display = ('identifier','long_name','date_added')
    list_filter = ['long_name']
    search_field =['identifier']

admin.site.register(Currency,CurrencyAdmin)

from my_app.models import Investor,Balances
class BalancesInline(admin.StackedInline):
    model = Balances
    extra = 2

class InvestorAdmin(admin.ModelAdmin):
    inlines = [BalancesInline]


admin.site.register(Investor,InvestorAdmin)

### Step 2 - register the player model so you can see it ###
### and the data on the site admin screen ###

from my_app.models import Player
class PlayerAdmin(admin.ModelAdmin):
    model = Player
admin.site.register(Player,PlayerAdmin)