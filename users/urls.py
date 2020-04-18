from . import views
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('update', views.update, name='update'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('shops', views.shops, name='shops'),
    path('clinic', views.clinic, name='clinic'),
    path('getstoreinfo', views.getstoreinfo, name='getstoreinfo'),
    path('getstorenews', views.getstorenews, name='getstorenews'),
    
]