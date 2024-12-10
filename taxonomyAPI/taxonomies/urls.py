from rest_framework.routers import DefaultRouter
from django.urls import path, include
from taxonomies.views import TaxonomyViewSet

router = DefaultRouter()
router.register(r'taxonomies', TaxonomyViewSet, basename='taxonomy')

urlpatterns = [
    path('', include(router.urls))
]