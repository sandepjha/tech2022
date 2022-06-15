


from tech import views
from django.urls import URLPattern
from django.urls import path

urlpatterns = [
    # path('',views.home),
    # path('',views.usersignup)
    path('',views.userlogin)
]