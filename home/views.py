from django.shortcuts import render,HttpResponse
from home.forms import CustomerForm
from home.forms import OrderForm
from home.forms import PaymentForm
# Create your views here.

def home_view(request):
    return render(request,'home.html')
def login_view(request):
    return render(request,'login.html')
def suvs_view(request):
    return render(request,'suv.html')
def sedans_view(request):
    return render(request,'sedan.html')
def sports_view(request):
    return render(request,'sports.html')
def convertibles_view(request):
    return render(request,'convertible.html')
def used_view(request):
    return render(request,'usedCar.html')
def audi_view(request):
    return render(request,'audi.html')
def bmw_view(request):
    return render(request,'bmw.html')
def honda_view(request):
    return render(request,'honda.html')
def landrover_view(request):
    return render(request,'landrover.html')
def toyota_view(request):
    return render(request,'toyota.html')
def mercedes_view(request):
    return render(request,'mercedes.html')
def payment_view(request):
    return render(request,'payment.html')
def view(request):
    return HttpResponse("<h1>SOLVED.</h1>")





def customer(request):


    form = CustomerForm()


    context = {
        'customer_form' : form,


    }



    return render(request,'customer.html',context)



def Order(request):


    form = OrderForm()


    context = {
        'order_form' : form,


    }



    return render(request,'order.html',context)


def Payment(request):


    form = PaymentForm()


    context = {
        'payment_form' : form,


    }



    return render(request,'payments.html',context)