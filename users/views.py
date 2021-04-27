from django.shortcuts import render

def add_user(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']

        context = {
            'username': username,
            'email': email,

        }

        return render(template_name='user_detail.html',
                      request=request,
                      context=context, )


    return render(template_name='add_user.html',
                  request=request,
                  context={},)