from apps.products.models import Category

def categories(request):
    return {
        'categories': Category.objects.filter(parent__isnull=True, is_active=True).prefetch_related('children')
    }
