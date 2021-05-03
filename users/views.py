from django.shortcuts import render, HttpResponse
from users.models import Users

def index(request):

    user = Users.objects.all()

    context = {
        'users': user
    }

    return render(template_name='index.html',
                  request=request,
                  context=context, )



def add_user(request):
    if request.method =='POST':

        users = Users(
            username=request.POST['username'],
            email=request.POST['email'],

        )
        users.save()

        context = {
            'username': users.username,
            'email': users.email,

        }

        return render(template_name='user_detail.html',
                      request=request,
                      context=context, )


    return render(template_name='add_user.html',
                  request=request,
                  context={},)


def get_user(request, user_id):

    user = Users.objects.get(pk=user_id)

    context = {
        'user': user,
    }

    return render(
        template_name='user.html',
        request=request,
        context=context,

    )


def delete_user(request, user_id):

    user = Users.objects.get(pk=user_id)
    user.delete()

    return HttpResponse(f'Deleted {user.username}')


def edit_user(request, user_id):

    user = Users.objects.get(id=user_id)

    if request.method == 'POST':

        username = request.POST['name']
        email = request.POST['email']

        if len(username) != 0:
            user.username = username

        if len(email) != 0:
            user.email = email

        user.save()

        context = {
            'user': user}

        return render(
            template_name='user.html',
            request=request,
            context=context,)

    return render(
        template_name='form.html',
        request=request)