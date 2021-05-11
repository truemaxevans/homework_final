from django.shortcuts import (
    render,
    HttpResponse,
    redirect,
)

from django.views.generic import (
    View,
    ListView,
    DetailView,
    FormView,
)

from django.urls import reverse_lazy

from user.models import User
from user.forms import UserForm


class UserListView(ListView):
    model = User
    template_name = 'index.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user.html'


class AddUserView(FormView):
    form_class = UserForm
    template_name = 'form.html'
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response


class EditUserView(View):

    def get(self, request, user_id):

        form = UserForm()

        context = {
            'form': form
        }

        return render(
            template_name='form.html',
            context=context,
            request=request,
        )

    def post(self, request, user_id):

        user = User.objects.get(id=user_id)

        username = request.POST['username']
        email = request.POST['email']

        if len(username) != 0:
            user.username = username

        if len(email) != 0:
            user.email = email

        user.save()

        return redirect(reverse_lazy('user-list'))


class DeleteUserView(View):

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        user.delete()

        return HttpResponse(f'Deleted {user.username}')
