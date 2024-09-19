from .models import Classification
from .models import Issue

def categories_processor(request):
    categories = Classification.objects.all()
    return {'categories': categories}

def issues_processor(request):
    issues = Issue.objects.all()
    return {'issues': issues}