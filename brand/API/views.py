from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import AdminBrandSerializer
from .renderers import BrandJSONRenderer
from brand.models import Brand
from core.permissions import IsSystemAdmin, IsSiteAdmin

# Create your views here.
class AdminBrandViewSet(viewsets.ModelViewSet):
    
    queryset = Brand.objects.all()
    serializer_class = AdminBrandSerializer
    permission_classes = (
        IsAuthenticated, 
        (IsSystemAdmin|IsSiteAdmin), 
        )
    renderer_classes = (BrandJSONRenderer, )