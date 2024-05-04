from django.http import HttpResponse
from django.shortcuts import redirect, render
from . forms import UserForm
from . models import User

def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # Create the user using model
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()

            return redirect('registerUser')
        else:
            print(form.errors)
            context = {
                'form': form
            }
            return render(request, 'auth/register.html', context)
    else:
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'auth/register.html', context)