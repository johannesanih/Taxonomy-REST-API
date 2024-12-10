from rest_framework import serializers
from taxonomies.models import Taxonomy

class TaxonomySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='taxonomy-detail', lookup_field='pk')

    class Meta:
        model = Taxonomy
        
        fields = [
            'url', 'id', 'name', 'male_name', 'female_name', 'reproductive_strategy', 'sex_determination', 'domain', 'kingdom', 'phylum', 'class_name', 'order', 'family', 'genus', 'species', 'description'
        ]
        
        extra_kwargs = { field: {'read_only': True} for field in fields}