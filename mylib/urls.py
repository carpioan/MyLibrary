from . import views
from .views import BookCreate
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.book_list, name='book_list'),
    url(r'^mylib/(?P<pk>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^mylib/new/$', BookCreate.as_view(),  name='book_new'),
    #url(r'^mylib/new/$', views.book_new, name='book_new'),
]