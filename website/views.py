from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import Group

from website.decorators import admin_only, unauthenticated_user
from .forms import AddMemberForm, CreateUser, AddCustomer


from django.contrib import messages
from .models import Members, Record
import hashlib

def generate_token(username, email):
    # Concatenate username, email, and some additional secret
    data = f"{username}{email}your_secret_salt_here"
    # Hash the concatenated data using SHA-256
    token = hashlib.sha256(data.encode()).hexdigest()
    return token
#@unauthenticated_user
#@admin_only    
def home(request):
    record = Record.objects.all()

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login successful, generate token and store it in the session
            token = generate_token(user.username, user.email)  # You need to define a function to generate token
            request.session['token'] = token
            login(request, user)
            messages.success(request, "You have logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials, please try again")
            return redirect('home')
    else:
        # Check if the user is already logged in using the token
        if 'token' in request.session:
            # Token exists, perform some action if needed
            pass
        else:
            # Token doesn't exist, perform some action if needed
            pass
        
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
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            group = form.cleaned_data['group']

            user.groups.add(group)  # Add user to the selected group
            user = authenticate(username=username, password=password)
            # login(request, user)  # Uncomment if you want to log in the user immediately after registration
            messages.success(request, 'You registered successfully')
            return redirect('home')
    else:
        form = CreateUser()
    return render(request, 'register.html', {'form': form})
    
    
    
  


#@admin_only
def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request, 'customer_record.html',{'customer_records':customer_record})
    else:
        messages.success(request,'you must be logged in to view customer records')
        return redirect('home')
#@admin_only    
def delete_customer(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Deleted customer record")
        return redirect('home')
    else:
        messages.success(request,'you must be logged in')
        redirect('home')
#@admin_only
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
    
def creaMember(request):
    form = AddMemberForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Member added successfully')
                return redirect('home')
            else:
                # Render the form with validation errors
                return render(request, 'add_member.html', {'form': form})
        else:
            # Handle GET requests or other methods
            return render(request, 'add_member.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to add a member.')
        return redirect('view_member')
    
def member_record(request, pk):
    if request.user.is_authenticated:
        member_record=Members.objects.get(id=pk)
        return render(request, 'view_member.html',{'member_records': member_record})
    else:
        messages.success(request,'you must be logged in to view member records')
        return redirect('home')

@admin_only
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
def custom_404(request, exception):
    return render(request, '404.html', status=404)
