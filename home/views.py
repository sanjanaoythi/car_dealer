from django.shortcuts import render,HttpResponse, redirect
#from home.forms import CustomerForm
#from home.forms import OrderForm
#from home.forms import PaymentForm
from home.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def registrationPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account created for ' + user)
            return redirect('login')

     
    context ={'form':form}
    return render(request, 'registration.html', context)
    
def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect' )
    
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')




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
    return render(request,'convertibles.html')
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

