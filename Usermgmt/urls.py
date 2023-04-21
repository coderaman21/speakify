from django.urls import path
from .views import userLogin,userLogout,userSignup
urlpatterns = [
    path("login", userLogin, name="login"),
    path("logout", userLogout, name="logout"),
    path('signup',userSignup,name='signup')
]