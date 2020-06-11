from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from inside.models import SanPham
from datetime import datetime
from inside.models import User
from . import forms
from cart.forms import CartAddProductForm
from django.contrib.auth import authenticate 
from django.contrib.auth import login
from django.contrib.auth import logout  

# Create your views here.
def index(request):
    SanPham_list = SanPham.objects.all()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1

    response = render(request, "inside/index.html", {'sanpham_list':SanPham_list, 'num_visits':num_visits})
    date1 = datetime.now()
    response.set_cookie("last_visit", date1.strftime('%d-%m-%Y %H:%M:%S'))
    last_visit = request.COOKIES.get('last_visit')

    return render(request, "inside/index.html", {'sanpham_list':SanPham_list, 'num_visits':num_visits, 'last_visit': last_visit})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                result = "WELCOME " + username
                return render(request, "inside/signin.html", {"result": result})
        else:
            print("Cannot Login")
            print("Username: {} and Password: {}".format(username, password))
            login_result = "Username and Password are not valid"
            return render(request, "inside/signin.html", {"result": login_result})
    else:
        return render(request, "inside/signin.html")

def user_logout(request):
    logout(request)
    result = "You have logged out, Please choose  SIGN IN"

    return render(request, "inside/logout.html", {"result":result})

def signup(request):
    form = forms.FormRegister()
    if request.method == 'POST':
        form =forms.FormRegister(request.POST, User)

        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['confirm']:
            request.POST._mutable = True
            post = form.save(commit = False)
            post.name = form.cleaned_data['name']
            post.email = form.cleaned_data['email']
            post.password = form.cleaned_data['password']
            post.save()
            print("Saved to database")

        elif form.cleaned_data['password'] != form.cleaned_data['confirm']:
            form.add_error('confirm', 'The password does not match')
            print("Not confirm!")
    return render(request, "inside/signup.html", {'form': form})

def chiTiet(request, id):
    sanPham = SanPham.objects.get(id=id)
    cart_product_form = CartAddProductForm()
    return render(request,'inside/chitiet.html',{'sanPham':sanPham, 'cart_product_form': cart_product_form})

def Registration(request):
    registered = False 
    if request.method == 'POST':
        form_user = forms.UserForm(data= request.POST)
        form_por = forms.UserProfileInfoForm(data= request.POST)
        if form_user.is_valid() and form_por.is_valid():
            user = form_user.save()
            user.set_password(user.password)
            user.save()

            profile = form_por.save(commit = False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
        else:
            print(form_user.errors, form_por.errors)

    else:
        form_user = forms.UserForm()
        form_por = forms.UserProfileInfoForm()

    return render(request, 'inside/registration.html', {'user_form': form_user, 'profile_form': form_por, 'registerd': registered})