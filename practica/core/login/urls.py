from django.urls import path
from .views import *
urlpatterns = [   
    path('', LoginFormView.as_view(), name="login"),
    # path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
]