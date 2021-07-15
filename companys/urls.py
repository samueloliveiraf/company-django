
from django.urls import path
from .views import list_company, company_page, submit_company


urlpatterns = [

    path('list-company/',
         list_company, name='home'),
    path('page/', 
        company_page),
    path('page/submit',
         submit_company),
    path('list-company/company/page/',
         company_page),
    path('list-company/company/page/submit',
        submit_company)
        
]
