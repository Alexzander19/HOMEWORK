from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import SignupForm

# Create your views here.

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      if request.POST.get("username") == 'admin':
        return  render(request, 'users/signup.html', {'error': 'Нельзя создать пользователя admin'})

      user.set_password(form.cleaned_data['password'])  # Хэшируем пароль
      user.save()
      
  else:
    form = SignupForm()
  return render(request, 'users/signup.html', {'form': form})


def signin(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    # Аутентификация пользователя
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)  # Вход пользователя
      return redirect('index')  # Перенаправление после успешного входа
    else:
      # Ошибка входа
      return render(request, 'users/signin.html', {'error': 'Неверный логин или пароль'})
  return render(request, 'users/signin.html')

def signout(request):
  # Выходим из системы
  logout(request)
  # Перенаправляем пользователя на страницу входа
  return redirect('signin')
