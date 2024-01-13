from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import CreateUser, AddCustomer


from django.contrib import messages
from .models import Record

def home(request):
    record=Record.objects.all()
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials, please try again")
            return redirect('home')
    else:
        # This is the modification for the GET request
        # You might want to customize this part based on your requirements
        return render(request, 'home.html', {'records': record})

    # This is added to handle the case when the method is a POST request
    #return HttpResponse("Invalid request method")
def logout_user(request):
    logout(request)
    messages.success(request,"User logged out")
    return render(request, 'home.html', {})



def register_user(request):
    if request.method =='POST':
        form=CreateUser(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            #login(request, user)
            messages.success(request, 'You registered successfully')
            return redirect('home')
    else:
        form=CreateUser()
        return render(request, 'register.html',{'form':form})
            
    return render(request, 'register.html',{'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request, 'customer_record.html',{'customer_records':customer_record})
    else:
        messages.success(request,'you must be logged in to view customer records')
        return redirect('home')
def delete_customer(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Deleted customer record")
        return redirect('home')
    else:
        messages.success(request,'you must be logged in')
        redirect('home')

def add_customer(request):
    form=AddCustomer(request.POST or None )
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            if form.is_valid():
                add_record=form.save()
                messages.success(request,'customer added successfully')
                return redirect('home')
        
                
        return render(request, 'add_record.html',{'form':form})
    else:
        messages.success(request,'you must logged first')
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        form=AddCustomer(request.POST or None, instance= customer_record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,'customer updated successfully')
                return redirect('home')
        else:
            return render(request, 'update_record.html',{'form':form})
    
    else:
        messages.success(request,'you must logged first')
        return redirect('home')

