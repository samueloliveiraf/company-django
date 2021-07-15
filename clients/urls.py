
from django.urls import path
from clients.views import (
    delete_clients,
    list_clients,
    submit_client,
    client_page
)

urlpatterns = [

    path('list/',
         list_clients,
         name='list-clients'
         ),
    path('list/page/',
         client_page
         ),
    path('list/client/list/page/',
         client_page
         ),
    path('list/page/submit',
         submit_client),
    path('list/client/list/page/submit',
         submit_client),
    path('list/client/list/delete/<int:id_client>/',
         delete_clients,
         ),
         
]
