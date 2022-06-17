from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def homepage_view(request):
    return render(request, 'user/index.html', {})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            # print(username)
            messages.success(request, f'Your account has been created. You can now login.')
            # storage = messages.get_messages(request)
            # for message in storage:
            return redirect('login')
            #     print(message)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg.capitalize()}: {form.error_messages[msg]}")
        # return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})

@login_required()
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
       
    }
    return render(request, 'user/profile.html', context)


def user_profile_update_view(request):
    if request.method == 'POST':
        pass