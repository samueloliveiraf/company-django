from django.shortcuts import redirect, render
from .models import Client
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


@login_required()
def client_page(request):
    id_client = request.GET.get('id')
    data = {}
    if id_client:
        data['client'] = Client.objects.get(id=id_client)
    return render(request, 'client_page.html', data)


@login_required
def list_clients(request):
    user = request.user
    client = Client.objects.filter(user=user)
    data = {'clients': client}
    return render(request, 'list_client.html', data)


@login_required
def delete_clients(request, id_client):
    user = request.user
    client = Client.objects.get(id=id_client)
    if user == client.user:
        client.delete()

    return redirect('list-clients')


@login_required
def submit_client(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        road = request.POST.get('road')
        district = request.POST.get('district')
        area_code = request.POST.get('area_code')
        city = request.POST.get('city')
        cep = request.POST.get('cep')
        user = request.user
        id_client = request.POST.get('id_client')
        if id_client:
            Client.objects.filter(
                id=id_client).update(
                name=name,
                email=email,
                phone_number=phone_number,
                road=road,
                district=district,
                area_code=area_code,
                city = city,
                cep = cep,
            )
        else:
            Client.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                road=road,
                district=district,
                area_code=area_code,
                city = city,
                cep = cep,
                user=user,
            )
    return redirect('list-clients')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
