from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'^contact/$',views.ContactPage.as_view(),name='contact'),
    url(r'^article/all/$',views.AllArticleAPIView.as_view())
]