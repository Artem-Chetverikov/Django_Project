from ftplib import error_perm
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UseForm


# Create your views here.
def sign_up_by_html(request):
    context = {}
    is_by_django = False
    context['is_by_django'] = is_by_django
    users = ['Andrey', 'Den', 'Serg']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if (password == repeat_password) and (age >= 18) and (username not in users):
            welcome = f'Приветствуем, {username}!'
            context['welcome'] = welcome
            return render(request, 'fifth_task/registration_page.html', context)
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)
        elif username  in users:
            info['error'] = 'Пользователь уже существует'
            context['info'] = info
            return render(request, 'fifth_task/registration_page.html', context)

    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    context = {}
    is_by_django = True
    context['is_by_django'] = is_by_django
    users = ['Andrey', 'Den', 'Serg']
    info = {}
    if request.method == 'POST':
        form = UseForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username_dj']
            password = form.cleaned_data['password_dj']
            repeat_password = form.cleaned_data['repeat_password_dj']
            age = int(form.cleaned_data['age_dj'])

            if (password == repeat_password) and (age >= 18) and (username not in users):
                welcome = f'Приветствуем, {username}!'
                context['welcome'] =  welcome
                return render(request, 'fifth_task/registration_page.html', context)
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                context['info'] = info
                return render(request, 'fifth_task/registration_page.html', context)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                context['info'] = info
                return render(request, 'fifth_task/registration_page.html', context)
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                context['info'] = info
                return render(request, 'fifth_task/registration_page.html', context)
    else:
        form = UseForm(request.POST)

    context['form'] = form
    return render(request, 'fifth_task/registration_page.html', context)




