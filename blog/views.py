from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Index(TemplateView):
    def get(self, request, **kwargs):
        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')[:9]

        for article in all_articles:
            article_data.append({
                'title':article.title,
                'cover':article.cover.url,
                'category':article.category,
                'created_at':article.created_at.date()
            })

        promote_data = []
        all_promote_articles = Article.objects.filter(promote=True)

        for article in all_promote_articles:
            promote_data.append({
                'category':article.category.title,
                'title':article.title,
                'created_at':article.created_at.date(),
                'author':article.author.user.first_name + ' ' + article.author.user.last_name,
                'avatar':article.author.avatar.url if article.author.avatar else None,
                'cover':article.cover.url if article.cover else None,
            })

        context = {
            'article_data':article_data,
            'promote_data':promote_data,
        }

        return render(request,'index.html',context)


class ContactPage(TemplateView):
    template_name = 'contact.html'


class AllArticleAPIView(APIView):

    def get(self,request,format=None):
        try:
            data = []
            all_articles = Article.objects.all().order_by('-created_at')[:9]

            for article in all_articles:
                data.append({
                    'title':article.title,
                    'cover':article.cover.url,
                    'content':article.content,
                    'created_at':article.created_at,
                    'category':article.category.title,
                    'author':article.author.user.first_name + ' ' + article.author.user.last_name,
                    'promote':article.promote,
                })

            return Response({'data':data},status.HTTP_200_OK)

        except:
            return Response({'error': "Retriving All Articles Failed!"}, status.HTTP_500_INTERNAL_SERVER_ERROR)