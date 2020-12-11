from django.shortcuts import render
from .models import Project
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from social.models import Link

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    links =Link.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(projects,2)

    try:
            projects =paginator.page(page)
    except PageNotAnInteger:
        projects =paginator.page(1)
    except EmptyPage:
        projects =paginator.page (paginator.num_pages)

    return render(request,"portfolio/portfolio.html",{'projects':projects},{'links':links})
