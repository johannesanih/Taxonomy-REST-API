from rest_framework import viewsets, status
from taxonomies.models import Taxonomy
from taxonomies.serializers import TaxonomySerializer

class TaxonomyViewSet(viewsets.ModelViewSet):
    queryset = Taxonomy.objects.all()
    serializer_class = TaxonomySerializer