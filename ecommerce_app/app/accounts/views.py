from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .forms import UserForm, ProfileForm
from .models import UserProfile


class BaseAccounts(View):
    template_name = 'create_accounts.html'

    def setup(self, *args, **kwargs) -> None:
        super().setup(*args, **kwargs)
        data = self.request.POST

        if self.request.user.is_authenticated:
            self.context = {'userform': UserForm(data=data, user=self.request.user, instance=self.request.user), 'userprofile': ProfileForm(data=data)}
        else:
            self.context = {'userform': UserForm(data), 'profileform': ProfileForm(data)}
            
        self.render = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.render



class AccountsListView(BaseAccounts):
    def post(self, *args, **kwargs):
        return self.render

class AccountsUpdateView(View):
      def get(self, *args, **kwargs):
        return HttpResponse('atl')


class LoginView(View):
    pass

class LogoutView(View):
    pass
