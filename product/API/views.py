from functools import partial
from rest_framework import status, mixins, viewsets

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import (
    Size, 
    Product
)
from .serializers import (
    ProductSerializer, SizeSerializer, Product
)

from .renderers import (
    SizeRenderer, ProductRenderer
)
from core.permissions import (
    IsSystemAdmin, IsSiteAdmin, IsMasterVendor, IsGeneralVendor
)

class SizeViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    
    queryset = Size.objects.all()
    renderer_classes = (SizeRenderer,)
    serializer_class = SizeSerializer
    
    # 추후에 Product를 category 별로 불러 오고 싶을 때 사용
    # List method에 적용됨      
    def get_queryset(self):
        queryset = self.queryset.filter(brand=self.request.user.brand)
        return queryset
    
    # viewset의 action에 따라 permission이 부여됨
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
            # CONTEXT에 request user의 brand 정보를 담아 Serializer에 보내면
            # serializer에서는 request user의 brand를 create할 때 인스턴스로 넣어줌
            # SizeSerializer()의 def create 부분 참고
            'brand': request.user.brand,
            'request': request
        }
        
        serializer_data = request.data
        serializer = self.serializer_class(
            data = serializer_data, context=serializer_context
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        data = self.paginate_queryset(self.get_queryset())
        
        serializer = self.serializer_class(
            data, many=True
        )
        return self.get_paginated_response(serializer.data)
    
    def partial_update(self, request, pk):
        serializer_context = {'request' : request}
        
        try:
            serializer_instance = self.queryset.get(pk=pk)
        except Size.DoesNotExist:
            raise NotFound('The size do not exist.')
        
        serializer_data = request.data
        serializer = self.serializer_class(
            serializer_instance,
            context = serializer_context,
            data = serializer_data,
            partial=True
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        try:
            data = self.queryset.get(pk=pk)
        except Size.DoesNotExist:
            raise NotFound('The size do not exist')
        
        data.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    
class ProductViewSet(
    viewsets.ModelViewSet
    ):
    
    queryset = Product.objects.all()
    renderer_classes = (ProductRenderer,)
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = self.queryset.filter(brand=self.request.user.brand)
        return  queryset
    
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
            'brand': request.user.brand,
            'request': request
        }
        print(request.data['subcategory'])
        serializer_data = request.data
        serializer = self.serializer_class(
            data = serializer_data, context=serializer_context
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        