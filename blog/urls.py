from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'^contact/$',views.ContactPage.as_view(),name='contact'),

    ### API
    url(r'^article/all/$',views.AllArticleAPIView.as_view(),name='all_articles'),
    url(r'^article$',views.SelectArticleAPIView.as_view(),name='select_article'),
    url(r'^article/search$',views.SearchArticleAPIView.as_view(),name='search_article'),
    url(r'^article/add$',views.AddArticleAPIView.as_view(),name='add_article'),
    url(r'^article/update$',views.UpdateArticleContentAPIView.as_view(),name='update_article'),
    url(r'^article/delete$',views.DeleteArticleAPIView.as_view(),name='delete_article'),
]