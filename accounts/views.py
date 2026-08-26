from .forms import RegistrationForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme


def signup(request):
	if request.user.is_authenticated:
		return redirect('profile')

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			redirect_to = request.POST.get('next')
			if redirect_to and url_has_allowed_host_and_scheme(
				url=redirect_to,
				allowed_hosts={request.get_host()},
				require_https=request.is_secure(),
			):
				return redirect(redirect_to)
			return redirect('home')
	else:
		form = RegistrationForm()

	return render(request, 'accounts/signup.html', {'form': form, 'next': request.GET.get('next', '')})


def login_view(request):
	if request.user.is_authenticated:
		return redirect('profile')

	redirect_to = request.GET.get('next', '')
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		redirect_to = request.POST.get('next', '')
		if form.is_valid():
			login(request, form.get_user())
			if redirect_to and url_has_allowed_host_and_scheme(
				url=redirect_to,
				allowed_hosts={request.get_host()},
				require_https=request.is_secure(),
			):
				return redirect(redirect_to)
			return redirect('home')
	else:
		form = AuthenticationForm(request)
	context = {
		'form': form,
		'next': redirect_to,
	}
	return render(request, 'accounts/login.html', context)


@login_required(login_url='login')
def profile_view(request):
	if request.method == 'POST':
		form = ProfileUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = ProfileUpdateForm(instance=request.user)

	return render(request, 'accounts/profile.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
	logout(request)
	return redirect('home')
