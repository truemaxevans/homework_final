from django.shortcuts import render
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