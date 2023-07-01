from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def form(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        # Process the form data or save it to the database

        # Optionally, you can redirect to a success page
        #return redirect('home.html')

    return render(request, 'home.html')



from django.shortcuts import render, redirect
from demoapp.models import Todo1
#from .forms import TodoForm

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:list')
    else:
        form = TodoForm()
    
    context = {
        'form': form,
    }
    return render(request, 'todo.html')


# views.py

from django.shortcuts import render, redirect
from .forms import MessageForm

def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to the home page or a success page
    else:
        form = MessageForm()
    
    return render(request, 'home.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def message_create(request):
    if request.method == 'POST':
        form = Message(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Message model
            return redirect('home')  # Redirect to the home page or any other desired page
    else:
        form = Message()
    
    return render(request, 'home.html', {'form': form})



from django.shortcuts import render
from .models import MyModel2,MyModel3
from demoapp.forms import MyForm
from demoapp.forms import MyForm1
def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'forms.html', {'form': form})


def my_form1(request):
  if request.method == "POST":
    form = MyForm1(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm1()
  return render(request, 'try41.html', {'form': form})
