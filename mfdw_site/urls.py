from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from quotes.views import Register
#from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('testpage', TemplateView.as_view(template_name='pages/page.html')),
    path('register/success/',TemplateView.as_view(template_name="registration/success.html"), name ='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('quote/', include('quotes.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
]
