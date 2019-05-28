from django.shortcuts import render
# from AppTwo.models import User
from . import forms

# Create your views here.

def index(request):
    return render(request, "AppTwo/index.html")

# def users(request):
#     user_list = User.objects.order_by("first_name")
#     user_dic = {"users" : user_list}
#     return render(request, "AppTwo/users.html", context=user_dic)

def form_name_view(request):
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            # Do something code
            form.save(commit = True)
            return index(request)
        else:
            print("Erro: Formulário Inválido")

    return render(request, "AppTwo/form_page.html", {'form': form})
    