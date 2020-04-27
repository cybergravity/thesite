from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Destination ,Item ,Customer,Calculation
# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

        
def index(request):
    if request.user.is_authenticated:
        bills = Destination.objects.all()
        params={
            'bills':bills
        }
        return render(request,'index.html',params)
    else:
        return redirect("/login")


def bill_view(request,unique_id):

    dest = Destination.objects.get(unique_id=unique_id)
    rest = Item.objects.filter(destination=dest).order_by('index')
    calc = Calculation.objects.get(destination=dest)
    customer = Customer.objects.get(destination=dest)
    
    print(unique_id)
    return render(request, "bill.html", {'dest': dest ,'rest': rest ,'customer':customer,'calc':calc})


