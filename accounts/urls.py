from django.urls import path
from .views import SignUpView, log_in, log_out

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
]
