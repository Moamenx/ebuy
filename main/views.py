from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import View
from main.models import *
import re
import requests
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




class HomeView(View):
    template_name = 'main/index.html'

    def get(self, request):
        cats = Category.objects.all()
        context = {'categories': get_categories(), 'news': get_news(), 'cats': cats, 'offers':get_offers()}
        return render(request, 'main/index.html', context)

    def post(self, request):
        if 'searchkey' in request.POST:
            print("I am in ")
            text = request.POST.get('searchkey', '')
            if text:
                product = Product.objects.all().filter(name__contains=text).exists()
                if product:
                    pro = Product.objects.get(name__contains=text)
                    cat = pro.category
                    catname = cat.name
                    print(cat)
                    return redirect('main:products', cat_name=catname.replace(' ', '-'), product_name=pro.name)


class BusinessView(View):
    template_name = 'main/business.html'

    def get(self, request):
        categories_names = get_categories()
        context = {'categories': categories_names, 'news': get_news()}
        return render(request, 'main/business.html', context)


def get_categories():
    cat_names = []
    categories = Category.objects.all()
    for category in categories:
        cat_names.append(category.name)
    categories_names = []
    for name in cat_names:
        categories_names.append(re.sub('\s+', '-', name))
    return categories_names


def get_news():
    news = []
    hot_news = HotNews.objects.all()
    if hot_news:
        for n in hot_news:
            news.append(n.news)
    return news


def get_currency(value, code):
    if code == "KWD":
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        return float("{0:.2f}".format(converted))
    elif code == 'OMR':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        return float("{0:.2f}".format(converted))
    elif code == 'BHD':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        return float("{0:.2f}".format(converted))
    elif code == 'AED':
        tax = float(value) * (5 / 100)
        final = float(value + tax)
        return float("{0:.2f}".format(final))
    elif code == 'JOD':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        price_with_tax = float(converted + (converted * (16 / 100)))
        return float("{0:.2f}".format(price_with_tax))
    elif code == 'SAR':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        price_with_tax = float(converted + (converted * (5 / 100)))
        return float("{0:.2f}".format(price_with_tax))
    elif code == 'QAR':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        result = json['AED_' + code]
        final = float(result * value)
        return float("{0:.2f}".format(final))
    elif code == 'LBP':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        price_with_tax = float(converted + (converted * (11 / 100)))
        return float("{0:.2f}".format(price_with_tax))


def get_offers():
    return Product.objects.filter(discount_rate__gt=0)


class ProductView(View):
    template_name = 'main/product.html'

    def get(self, request, cat_name, product_name):
        productName = product_name.replace('-', ' ')
        isProduct = True

        if Product.objects.all().filter(name=productName).exists():
            try:
                product = Product.objects.get(name=productName)
                product_photos = ProductPhoto.objects.all()
            except (Product.DoesNotExist, ProductPhoto.DoesNotExist):
                product_photos = None
                product = None
            context = {'item': product, 'category': cat_name, 'categories': get_categories(), 'isProduct': isProduct,
                       'product_photos': product_photos, 'news': get_news(), 'offers': get_offers()}

        else:
            isProduct = False
            try:
                package = Package.objects.get(name=productName)
                package_photos = PackagePhoto.objects.all()
                package_products = PackageProduct.objects.all().filter(package=package)
            except (Package.DoesNotExist, PackagePhoto.DoesNotExist):
                package_photos = None
                package = None
                package_products = None

            context = {'item': package, 'category': cat_name, 'categories': get_categories(), 'isProduct': isProduct,
                       'packagephotos': package_photos, 'packageproducts': package_products, 'news': get_news(),
                       'offers': get_offers()}

        return render(request, 'main/product.html', context)

    def post(self, request, cat_name, product_name):
        quantity = request.POST.get('quantity', 1)
        currency = self.request.POST.get('currency', 'usd')
        name = request.POST.get('itemName')
        id = request.POST.get('itemId')
        item_type = request.POST.get('type')
        price = request.POST.get('price')
        item_to_add = {

            "id": id,
            "quantity": quantity,
            "price": price,
            "currency": currency,
            "type": item_type,

        }
        if 'cart_names' not in request.session:
            request.session['cart_names'] = []
        if 'cart' not in request.session:
            request.session['cart'] = {'items': {}}
        dict = request.session.get("cart", {})
        dict['items'][name] = item_to_add
        request.session['cart'] = dict
        return HttpResponseRedirect(self.request.path_info)


class CategoryView(View):
    template_name = 'main/category.html'

    def get(self, request, cat_name):
        category_name = cat_name.replace('-', ' ')
        category = Category()
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            category = None
        try:
            products = Product.objects.all().filter(category=category)
            product_photos = ProductPhoto.objects.all()
        except Product.DoesNotExist:
            products = None
            product_photos = None
        try:
            packages = Package.objects.all().filter(category=category)
            package_photos = PackagePhoto.objects.all()
        except Package.DoesNotExist:
            packages = None
            package_photos = None
        context = {'categoryurl': cat_name, 'products': products, 'packages': packages, 'categoryName': category_name,
                   'categories': get_categories(), 'productphotos': product_photos, 'packagephotos': package_photos,
                   'active': 'active', 'news': get_news(), 'offers':get_offers()}

        return render(request, 'main/category.html', context)


class AboutView(View):
    template_name = 'main/about.html'

    def get(self, request):

        context = {'categories': get_categories(), 'news': get_news()}
        return render(request, 'main/about.html', context)


def listing(request):
    contact_list = Product.objects.all()
    paginator = Paginator(list(contact_list), 1)

    page = request.GET.get('page')
    contacts = paginator.page(page)
    return render(request, 'main/list.html', {'contacts': contacts})


class ContactUsView(View):
    template_name = 'main/contact.html'

    def get(self, request):
        context = {'categories': get_categories(), 'news': get_news()}
        return render(request, 'main/contact.html', context)

    def post(self, request):
        email = self.request.POST.get('email')
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            context = {'categories': get_categories(), 'msg': 'Invalid email address'}
            return render(request, 'main/contact.html', context)
        phone = self.request.POST.get('phone')
        message = self.request.POST.get('message')
        name = self.request.POST.get('name')
        # if name and message and phone!= "":
        send_mail("Business User",
                  "Name: " + name + "\n" + "User Email: " + email + "\n" + "User Phone: " + phone + "\n" + "Message: " + message,
                  settings.EMAIL_HOST_USER, ['20140165@fa-hists.edu.eg'], fail_silently=False)
        messages.success(request, 'Thank you for sending us an email!')
        return render(request, 'main/contact.html')


class RegistrationView(View):
    template_name = 'main/registration.html'

    def get(self, request):
        context = {'categories': get_categories(), 'news': get_news()}
        return render(request, 'main/registration.html', context)

    def post(self, request):
        print("Hello")
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        con_password = request.POST.get('conpassword')
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phonenumber')
        if username =="" or email != "" or first_name != "" or last_name == "" or phone == "":
            print("I am in")
            messages.add_message(request, messages.ERROR, 'برجاء التأكد من ادخال جميع البينات')
            return render(request, 'main/registration.html')
        if username != "" and email != "" and first_name != "" and last_name != "" and phone != "" :
            if password == con_password :
                user = User.objects.create(username=username, password=make_password(password), email=email,
                                           first_name=first_name, last_name=last_name)
                UserProfile.objects.create(user=user, phone_number=phone)
                messages.add_message(request, messages.SUCCESS, 'Your account registered successfully.')
                return render(request, 'main/registration.html')
        else:
            messages.add_message(request, messages.ERROR, 'Emtpy fields. Please try again.')
            return render(request, 'main/registration.html')


class LoginView(View):
    template_name = 'main/login.html'

    def get(self, request):

        if self.request.user.is_authenticated:
            return redirect('/home')
        else:

            context = {'news': get_news(), 'categories': get_categories(), 'offers':get_offers()}
            return render(request, 'main/login.html', context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username=username, password=password)
        if auth is not None:
            user = User.objects.get(username=username)
            login(request, user)
            request.session['username'] = username
            return redirect(request.META.get('HTTP_REFERER'), {'username': username})
        else:
            return redirect(self.request.path_info, {'msg': 'Incorrect username or password'})


class CartView(View):
    template_name = "main/cart.html"

    def get(self, request):

        if not self.request.user.is_authenticated:
            return redirect('/home/login')
        else:
            context = {'news': get_news(), 'categories': get_categories()}
            return render(request, 'main/cart.html', context)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def order(request):
    return render(request, 'main/checkout.html')
