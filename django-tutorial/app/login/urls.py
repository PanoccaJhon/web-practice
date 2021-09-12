from django.urls import path
from login.views import LoginFormView, LogoutView, LogoutRedirectView



app_name = 'user'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='user:login'), name = 'logout'),
    #path('logout/', LogoutRedirectView.as_view(), name = 'logout'),
]