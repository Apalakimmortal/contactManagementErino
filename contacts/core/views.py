from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import User as CustomUserModel

def user_list_create(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        company = data.get('company')
        job_title = data.get('job_title')

        if CustomUserModel.objects.filter(email=email).exists() or CustomUserModel.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "User with this email or phone number already exists.")
            return redirect('/contacts/')

        CustomUserModel.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            company=company,
            job_title=job_title,
        )
        messages.success(request, "User created successfully.")
        return redirect('/contacts/')

    queryset = CustomUserModel.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(first_name__icontains=request.GET.get('search'))
    
    context = {'users': queryset}
    return render(request, 'users.html', context)


# Delete a user
def delete_user(request, id):
    user = get_object_or_404(CustomUserModel, id=id)
    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('/contacts/')


# Update a user
def update_user(request, id):
    user = get_object_or_404(CustomUserModel, id=id)

    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        company = data.get('company')
        job_title = data.get('job_title')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.phone_number = phone_number
        user.company = company
        user.job_title = job_title
        user.save()

        messages.success(request, "User updated successfully.")
        return redirect('/contacts/')
    
    context = {'user': user}
    return render(request, 'update_user.html', context)