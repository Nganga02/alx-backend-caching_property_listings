
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property

# Cache this view for 15 minutes
@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values(
        'id', 'title', 'description', 'price', 'location', 'created_at'
    )
    return JsonResponse(list(properties), safe=False)


from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties()

    # Convert objects to dict for JSON response
    properties_data = [
        {
            'id': prop.id,
            'title': prop.title,
            'description': prop.description,
            'price': str(prop.price),  # Decimal to string
            'location': prop.location,
            'created_at': prop.created_at.isoformat(),
        }
        for prop in properties
    ]

    return JsonResponse(properties_data, safe=False)