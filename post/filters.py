from django.db.models import fields
import django_filters
from .models import mypost

class myfilter(django_filters.FilterSet):

    class Meta:
        model=mypost
        fields=('user', 'City', 'service_provider')
