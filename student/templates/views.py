from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf.urls import include
from django.template import loader
from .models import Student
from django.http import Http404
from .forms import SignUpForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')



def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  
			user.student.student_name = form.cleaned_data.get('teacher_name')
			user.student.student_name = form.cleaned_data.get('email')
			user.student.student_name = form.cleaned_data.get('phone_number')
			user.refresh_from_db()
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
@login_required
def change_password(request):
    print ('POST')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            #update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was updated successfully!')  # <-
            return redirect('home')
        else:
            messages.warning(request, 'Please correct the error below.')  
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})