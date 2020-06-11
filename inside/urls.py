from django.conf.urls import url
from inside import views

app_name = 'inside'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'signin', views.signin, name = 'signin'),
    url(r'signup', views.signup, name = 'signup'),
    url(r'logout', views.user_logout, name = 'logout'),
    url(r'chi-tiet/(\d+)$', views.chiTiet,name='chi-tiet'),
    url(r'registered', views.Registration,name='registered'),
]