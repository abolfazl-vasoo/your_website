from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

# Create your views here.
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from user.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from user.models import User
from utils.email_service import send_email
# from django.core.mail import send_mail



class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'user/user.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate_account.html')
                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }

        return render(request, 'user/user.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'user/user.html', context)


    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('user_panel_dashboard'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'user/user.html', context)




class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm()
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'user/forgot_password.html', context)

    def post(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forgot_password.html')
                return redirect(reverse('home_page'))

        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'user/forgot_password.html', context)

class ResetPassword(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))

        reset_pass_form = ResetPasswordForm()

        context = {'reset_pass_form': reset_pass_form}
        return render(request, 'user/reset_password.html', context)