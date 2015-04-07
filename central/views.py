from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from models import User

def user_can_see(user):
    return user.is_superuser or user.groups.filter(name='UsersCentral').exists()

@login_required
@user_passes_test(user_can_see, login_url='/map/')
def central_home(request):
    context = {'user': request.user}
    return render(request, 'central_home.html', context)


def central_create(request):
    context = {'user': request.user}
    return render(request, 'central_create.html', context)

@login_required
def central_owner_principal(request):
    context = {'user': request.user}
    return render(request, 'owner_principal.html', context)

@login_required
def central_individual_load(request):
    context = {'user': request.user}
    return render(request, 'owner_individual_load.html', context)

@login_required
def central_huge_load(request):
    context = {'user': request.user}
    return render(request, 'owner_huge_load.html', context)

@login_required()
def create_owner(request):
    user = User()
    if 'username' in request.POST and request.POST['username']:
        user.username = request.POST['username']

    if 'name' in request.POST and request.POST['name']:
        user.first_name = request.POST['name']

    if 'lastname' in request.POST and request.POST['lastname']:
        user.last_name = request.POST['lastname']

    if 'email' in request.POST and request.POST['email']:
        user.email = request.POST['email']

    if 'pass' in request.POST and request.POST['pass']:
        user.password = request.POST['pass']
    user.is_superuser = 'f'
    user.is_active = 't'
    user.is_staff = 'f'
    user.save()
