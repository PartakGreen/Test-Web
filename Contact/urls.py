from django.conf.urls import url

from . import views
urlpatterns = [
    # new url definition
    #url(r'^Contact/$', views.contact, name='contact')
    url(r'^$', views.contact, name='contact')

]