from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'^contact/$',views.ContactPage.as_view(),name='contact'),

    ### API
    url(r'^article/all/$',views.AllArticleAPIView.as_view(),name='all_articles'),
    url(r'^article/$',views.SelectArticleAPIView.as_view(),name='select_article')
]