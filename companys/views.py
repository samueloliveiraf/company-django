
from django.shortcuts import render, redirect
from .models import Company
from django.contrib.auth.decorators import login_required


@login_required
def list_company(request):
    user = request.user
    company = Company.objects.filter(user=user)
    data = {'companys': company, 'user': user}
    return render (request, 'index.html', data)


@login_required
def submit_company(request):
    if request.POST:
        name_company = request.POST.get('name_company')
        user = request.user
        id_company = request.POST.get('id_company')
        if id_company:
            Company.objects.filter(
                id=id_company).update(
                name_company=name_company
            )
        else:
            Company.objects.create(
                name_company=name_company,
                user=user
            )
    return redirect('home')


@login_required()
def company_page(request):
    id_client = request.GET.get('id')
    data = {}
    if id_client:
        data['companys'] = Company.objects.get(id=id_client)
    return render(request, 'company_page.html', data)

