from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main.views import *

app_name = 'main'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'about-us/', AboutView.as_view(), name='about'),
    url(r'contact-us/', ContactUsView.as_view(), name='contact'),
    url(r'registration/', RegistrationView.as_view(), name='registration'),
    url(r'login/', LoginView.as_view(), name='login'),
    #url(r'search/', include('haystack.urls'), name='search'),
    #url(r'test/', listing, name=''),
    url(r'logout/', LogoutView.as_view(), name='logout'),
    url(r'cart/', CartView.as_view(), name='cart'),
    url(r'business/', BusinessView.as_view(), name='business'),
    url(r'^categories/(?P<cat_name>[\w|\W]+)/', CategoryView.as_view(), name='categories'),
    url(r'^products/(?P<cat_name>[\w|\W]+)/(?P<product_name>[\w|\W]+)', ProductView.as_view(), name='products'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

import threading
from main import currency

#threading.Timer(86400,currency.currency_converter()).start()

