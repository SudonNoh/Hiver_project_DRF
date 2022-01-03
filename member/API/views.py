from rest_framework.decorators import authentication_classes, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import AdminBrandSerializer
from .renderers import BrandJSONRenderer
from member.models import Brand
from core.permissions import IsStaffOnly

# Create your views here.
class AdminBrandViewSet(viewsets.ModelViewSet):
    
    queryset = Brand.objects.all()
    serializer_class = AdminBrandSerializer
    permission_classes = (IsAuthenticated, IsStaffOnly, )
    renderer_classes = (BrandJSONRenderer, )