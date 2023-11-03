from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache
from .models import Person
from django.contrib import messages




# Create your views here.
@never_cache
def loginn(request):
    if 'name' in request.session:
        return redirect('crud')
    if 'username' in request.session:
        return redirect('logout')
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            m = Person.objects.get(username=username)
            if m.password==password:
                request.session['username'] = username
                return redirect('logout')
        except:
            pass
        
        messages.error(request, "Username or Password Incorrect") 
            
    return render(request,'login.html')


# @never_cache
# def signupp(request):
#     if 'username' in request.session:
#         return redirect('logout')
    
  
@never_cache
def signupp(request):
    if 'name' in request.session:
        return redirect('crud')
    if 'username' in request.session:
        return redirect('logout')
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        mobile_number = request.POST["mobile_number"]
        password = request.POST["password"]
        cp = request.POST["cp"]  

        if Person.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            
        elif Person.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            
        elif Person.objects.filter(mobile_number=mobile_number).exists():
            messages.error(request, "Mobile Number already exists")
            
        elif len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long")
            
        elif password != cp:
            messages.error(request, "Passwords does not match")       
        else:
            myuser = Person.objects.create(username=username, email=email, password=password, mobile_number=mobile_number)
            myuser.save()
            # messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    return render(request, 'signup.html')


@never_cache
def logoutt(request):
    if 'name' in request.session:
        return redirect('crud')
    if 'username' in request.session:
        username = request.session['username']
        return render(request, 'logout.html',{'username':username})
    else:
        return redirect('login')


@never_cache
def adminloginn(request):
    if 'name' in request.session:
        return redirect('crud') 
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['name'] = username
            return redirect('crud')
        else:
            return redirect('adminlogin')
    return render(request, 'adminlogin.html')


def user_logout(request):
    if 'username' or 'name' in request.session:
        request.session.flush()
    return redirect('login')


@never_cache
def crudd(request):
    if 'name' not in request.session:
        return redirect('login') 
    empl = Person.objects.all()
    context = {
        'empl':empl,
    }
    return render(request, 'crud.html',context)


@never_cache
def addd(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        
        if Person.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            
        elif Person.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            
        elif Person.objects.filter(mobile_number=mobile_number).exists():
            messages.error(request, "Mobile Number already exists")
            
        elif len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long")
        else:
            empl = Person(username=username, email=email, mobile_number=mobile_number, password=password)
            empl.save()
            messages.success(request, "Succesfully Created")

        return redirect('crud')       


# def editt(request):
#     empl = Person.objects.all()
#     context = {
#         'empl':empl,
#     }
#     return render(request, 'crud.html',context)

def Update(request,id):
    if 'name' not in request.session:
        return redirect('login') 
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        empl = Person(id = id,
                      username=username,
                      email=email,
                      mobile_number=mobile_number,
                      password=password)  
        empl.save()
        return redirect('crud')
        
    return render(request, 'crud.html')

def deletee(request,id):
    if 'name' not in request.session:
        return redirect('login') 
    if 'username' in request.session:
        return redirect('login')
    empl = Person.objects.filter(id=id)
    empl.delete()
    return redirect('crud')
@never_cache
def searchh(request):
    if 'name' in request.session:
        query = request.GET['query']
        allPosts = Person.objects.filter(username__icontains = query)
        context = {'allPosts': allPosts}
        return render(request, 'search.html', context)
    else:
        return redirect('login')
    

