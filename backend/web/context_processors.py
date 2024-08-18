from .models import Classification

def categories_processor(request):
    categories = Classification.objects.all()
    return {'categories': categories}