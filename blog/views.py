from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class Index(TemplateView):
    def get(self, request, **kwargs):
        article_data = []
        all_articles = Article.objects.all()[:9]

        for article in all_articles:
            article_data.append({
                'title':article.title,
                'cover':article.cover,
                'category':article.category,
                'created_at':article.created_at
            })

        context = {
            'article_data':article_data
        }

        return render(request,'index.html',context)

