from django.shortcuts import render, HttpResponse,get_object_or_404
from my_app.models import Currency, Investor, Player ### See 7 - import player model ###
# Create your views here.

### See 6.b - I am passing all of the Player objects into the template ###
def home1(request):
    context = dict()
    context['Players'] = Player.objects.all()
    return render(request,"home.html",context)

def home(request):
    context = dict()
    return render(request,"home1.html",context)

def guest(request):
    context = dict()
    currency_list = Currency.objects.all()
    context['currency_list'] = currency_list
    return render(request,"guest.html",context)

def loggedIn(request):
    context = dict()
    the_user = request.user
    investor = Investor.objects.get(user=the_user)
    context['investor'] = investor
    return render(request,'loggedIn.html',context)


def detail(request,currency_id):
    context=dict()
    currency = get_object_or_404(Currency,identifier=currency_id)
    context['currency']=currency
    print(currency)
    return render(request, 'detail.html', context)

def exchange_rates(request,currency_id):
    c=get_object_or_404(Currency,identifier=currency_id)
    amount=request.GET['Conversion_Amount']
    cross_c=c.rates_set.get(pk=request.GET['Cross_Currency_List'])
    try:
        float(amount)
    except:
        return render(request, 'detail.html', {'currency':c})
    output="The current conversion rate from " + currency_id + " to  " +cross_c.id_2
    output=output + " is: " + str(cross_c.rate)+". "
    output=output+ currency_id + ' ' + str(amount) + " is equal to " + cross_c.id_2 + ' '
    output=output+str(float(amount)*float(cross_c.rate))
    return HttpResponse(output)
