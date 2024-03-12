from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate


signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="account/form.html",
    success_url=settings.LOGIN_URL,
)


login = LoginView.as_view(
    template_name="account/form.html",
    # success_url=settings.LOGIN_REDIRECT_URL,
    # next_page=settings.LOGIN_REDIRECT_URL,
)


logout = LogoutView.as_view(
    next_page=settings.LOGOUT_URL,
)


@login_required
def profile(request):
    return render(request, "account/profile.html")


def logincheck(request):
    if request.user.is_authenticated:
        return HttpResponse("로그인 됨!")
    return HttpResponse("로그인 안됨!!")
    

def logincheck(request):
    print(request.user.is_authenticated)
    print(request.user)
    print(type(request.user))
    print(dir(request.user))
    return render(request, 'account/logincheck.html')

def loginfbv(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        print(type(user))
        if user is not None:
            login(request, user)
            return HttpResponse("login 성공")
        else:
            return HttpResponse("login 실패")
    return render(request, "accounts/loginfbv.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog:blog_list')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})