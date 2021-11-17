from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator

def articleview(request):
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj':page_obj})
