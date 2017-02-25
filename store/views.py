from django.shortcuts import render, get_object_or_404, redirect
from .models import Mobile, Brand, Sold
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SoldForm, UserForm
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'index.html', {})


@login_required
def myboughtlist(request):
    sold = Sold.objects.filter(customer=request.user)
    return render(request, 'myboughtlist.html', {'sold': sold})


@login_required
def info(request, slug):
    mob = get_object_or_404(Mobile, slug=slug)
    quant = mob.repository
    user = request.user
    email = user.email
    fname = user.first_name
    lname = user.last_name
    if request.method == "POST":
        form = SoldForm(request.POST, quant=quant)
        if form.is_valid():
            sold = form.save(commit=False)
            sold.customer = request.user
            sold.brand = mob.brand
            sold.product = mob.name
            sold.date = timezone.now()
            sold.save()
            return buy(request, sold, slug)
    else:
        form = SoldForm(quant=quant)
    return render(request, 'info.html', {'form': form, 'mob': mob, 'user': user,
                                         'email': email, 'fname': fname, 'lname': lname})


@login_required
def buy(request, sold, slug):
    mob = get_object_or_404(Mobile, slug=slug)
    time = timezone.now()
    user = request.user
    email = user.email
    fname = user.first_name
    lname = user.last_name
    if mob.repository > 1:
        mob.repository = mob.repository - sold.amount
    elif mob.repository == 1:
        mob.repository = mob.repository - sold.amount
        mob.status = 'u'
    else:
        mob.status = 'u'
    mob.save()
    num = mob.repository
    return render(request, 'buy.html', {'num': num, 'mob': mob, 'sold': sold, 'time': time,
                                        'user': user, 'email': email, 'fname': fname, 'lname': lname})


@login_required
def pay(request, slug):
    mob = get_object_or_404(Mobile, slug=slug)
    price = mob.price
    user = request.user
    email = user.email
    fname = user.first_name
    lname = user.last_name
    return render(request, 'pay.html', {'price': price, 'email': email, 'fname': fname, 'lname': lname})


def mobilelistview(request):
    mobiles = Mobile.objects.all()
    paginator = Paginator(mobiles, 10)

    page = request.GET.get('page')
    try:
        mobiles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mobiles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        mobiles = paginator.page(paginator.num_pages)

    return render(request, 'store/mobile_list.html', {'mobiles': mobiles})


def mobiledetailview(request, slug):
    mobiles = get_object_or_404(Mobile, slug=slug)
    if mobiles.repository > 0:
        mobiles.status = 'a'
        mobiles.save()
    return render(request, 'store/mobile_detail.html', {'mobiles': mobiles})


def brandlistview(request):
    brands = Brand.objects.all()
    return render(request, 'store/brand_list.html', {'brands': brands})


def branddetailview(request, slug):
    brands = get_object_or_404(Brand, slug=slug)
    mobs = Mobile.objects.filter(brand__name=brands.name)
    return render(request, 'store/brand_detail.html', {'brands': brands, 'mobs': mobs})


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect('signupsuccess')
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})


def signupsuccess(request):
    return render(request, 'signup-success.html', {})
