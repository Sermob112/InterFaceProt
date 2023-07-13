

from django.contrib.auth import views as auth_views, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import *
from .models import DataPoint




def register(request):
    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован!')
            default_role = Role.objects.get(name='Работник')  # Replace 'пользователь' with the name of your default role
            user = CustomUser.objects.get(username=username)
            user.role = default_role
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    return render(request, 'base.html')

# def custom_logout(request):
#     # Redirect to a specific page after logout
#     return auth_views.LogoutView.as_view(next_page='index')(request)
#График
def chart_view(request):
    data_points = DataPoint.objects.all()
    return render(request, 'chart.html', {'data_points': data_points})
# def chart_data(request):
#     data_points = DataPoint.objects.order_by('x')
#     labels = [str(data_point.x) for data_point in data_points]
#     data = [data_point.y for data_point in data_points]
#
#     chart_data = {
#         'labels': labels,
#         'datasets': [
#             {
#                 'data': data,
#                 'backgroundColor': 'rgba(202, 201, 197, 0.5)',
#                 'borderColor': 'rgba(202, 201, 197, 1)',
#                 'pointBackgroundColor': 'rgba(202, 201, 197, 1)',
#                 'pointBorderColor': '#fff',
#             }
#         ]
#     }
#
#     return JsonResponse(chart_data)


@login_required
@user_passes_test(lambda user: user.role.name == 'Директор')
def director_view(request):
    # Ваша логика для представления директора
    return render(request, 'director_dashboard.html')


# Представление для роли "Конструктор"
@login_required
@user_passes_test(lambda user: user.role.name == 'Конструктор')
def constructor_view(request):
    # Ваша логика для представления конструктора
    return render(request, 'constructor.html')


# Представление для роли "Работник"
@login_required
@user_passes_test(lambda user: user.role.name == 'Работник')
def worker_view(request):
    # Ваша логика для представления работника
    return render(request, 'worker.html')

# def custom_login(request):
#     if request.user.is_authenticated:
#         return redirect('index')  # Redirect authenticated users to a specific page if needed.
#     else:
#         return auth_views.LoginView.as_view(template_name='login.html')(request)

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('index')  # Перенаправление на стартовую страницу, если пользователь уже авторизован

    # Обработка отправки формы авторизации
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)  # Перенаправление на URL из параметра next
            else:
                return redirect('index')  # Перенаправление на стартовую страницу, если параметр next не указан

    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})
def custom_logout(request):
    return auth_views.LogoutView.as_view()(request)