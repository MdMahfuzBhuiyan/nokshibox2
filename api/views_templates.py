from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Category, User
from .forms import UserSignupForm, UserLoginForm, ProductForm
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

# Landing page for buyer or unregistered user
def base(request):
    return render(request, 'base.html')
def buyer_home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'buyer_home.html', {'products': products, 'categories': categories})

# Signup page
def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate using backend
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)  # session now persists

                # Redirect to ?next if present and safe
                next_url = request.POST.get('next') or request.GET.get('next')
                if next_url and url_has_allowed_host_and_scheme(next_url, settings.ALLOWED_HOSTS):
                    return redirect(next_url)

                # Fallback: role-based redirect
                if user.role == 'seller':
                    return redirect('seller_home')
                return redirect('buyer_home')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {
        'form': form,
        'next': request.GET.get('next', '')
    })

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Seller landing page
@login_required
def seller_home(request):
    print("DEBUG: request.user:", request.user)
    print("DEBUG: is_authenticated:", request.user.is_authenticated)
    if request.user.role != 'seller':
        return redirect('buyer_home')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('seller_home')
    else:
        form = ProductForm()
    my_products = Product.objects.filter(seller=request.user)
    return render(request, 'seller_home.html', {'form': form, 'my_products': my_products})

# Product detail page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Seller detail page
def seller_detail(request, pk):
    seller = get_object_or_404(User, pk=pk, role='seller')
    seller_products = Product.objects.filter(seller=seller)
    return render(request, 'seller_detail.html', {'seller': seller, 'products': seller_products})
