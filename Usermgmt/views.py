from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from Usermgmt.serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from Home.models import ChatRoom
from django.db.models import Q

# Create your views here.
def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        # authenticate the user
        user = authenticate(request,username=username,password=password)

        if user is not None:
            if not user.is_active :
                messages.error(request,"Your account is not active, please confirm your email to activate your account ")   
                return render(request, "login.html")
            else:
                login(request,user)
                return redirect('home')
        else: 
            messages.error(request,"Couldn't login check your username or password again")
    
    return render(request, "login.html")

def userSignup(request):
    if request.method == 'POST':
      
        request.POST._mutable = True
        password = request.POST.pop('password')[0]
        csrfToken = request.POST.pop('csrfmiddlewaretoken')

        serializer = UserSerializer(data = request.POST)
        if serializer.is_valid() :
            user = serializer.save(password = make_password(password))
            login(request,user)
            return redirect('home')
        messages.error(request,f"{serializer.errors}")
        return render(request,'signup.html')
    return render(request,'signup.html')

def userLogout(request):
    user = request.user
    user.is_online = False
    user.save()
    logout(request)
    ChatRoom.objects.filter(Q(user1 = user)|Q(user2 = user)).delete()

    return redirect('home')
