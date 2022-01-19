from distutils.command.sdist import sdist
from rest_framework import status, mixins, viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import (
    Size, 
    Product
)
from .serializers import (
    SizeSerializer,
)

from .renderers import (
    SizeRenderer,
)
from core.permissions import (
    IsSystemAdmin, IsSiteAdmin, IsMasterVendor, IsGeneralVendor
)

class SizeViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    
    queryset = Size.objects.all()
    renderer_classes = (SizeRenderer,)
    serializer_class = SizeSerializer
    
    # 추후에 Product를 category 별로 불러 오고 싶을 때 사용
    # List method에 적용됨      
    def get_queryset(self):
        queryset = self.queryset.filter(brand_id=self.request.user.brand)
        return queryset
    
    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [
                IsAuthenticated, 
                (IsSystemAdmin|IsSiteAdmin|IsMasterVendor),
                ]
        else:
            permission_classes = [
                IsAuthenticated,
                (IsSystemAdmin|IsSiteAdmin|IsMasterVendor|IsGeneralVendor)
                ]
        return [permission() for permission in permission_classes]
    
    def create(self, request):
        serializer_context = {
            'brand_id': request.user.brand,
            'request': request
        }
        print('serializer_context : ', serializer_context)
        
        serializer_data = request.data
        serializer = self.serializer_class(
            data = serializer_data, context=serializer_context
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        page = self.paginate_queryset(self.get_queryset())
        
        serializer = self.serializer_class(
            page, many=True
        )
        return self.get_paginated_response(serializer.data)