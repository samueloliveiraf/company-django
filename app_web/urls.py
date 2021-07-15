
from django.contrib import admin
from django.urls import path, include
from companys.views import list_company
from clients.views import SignUp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_company),
    path('company/', 
        include('companys.urls')),
    path('clients/', 
        include('clients.urls')),
    path('accounts/', 
        include('django.contrib.auth.urls')),
    path('register/', SignUp.as_view(), name="signup"),
]
