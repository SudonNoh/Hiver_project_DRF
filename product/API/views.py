from rest_framework import status, mixins, viewsets

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import (
    Size, Product, Product_Image
)
from .serializers import (
    ProductSerializer, SizeSerializer, Product_ImageSerializer
)
from .renderers import (
    SizeRenderer, ProductRenderer, Product_ImageRenderer
)
from core.permissions import (
    IsSystemAdmin, IsSiteAdmin, IsMasterVendor, IsGeneralVendor
)

class SizeViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    # UpdateModelMixin을 상속받지 않은 상태에서 partial_update가 동작하는 것을 보고
    # 의구심이 들었다. 그래서 다른 동작도 되지 않는지 확인해보았다.
    
    # 기존에 mixins.CreateModelMixin과 mixins.DestroyMixin을 상속 받았었는데,
    # 두 가지 모두 주석처리 해도 POST와 DELETE가 동작하는 것이었다. 다만 get 요청은
    # 동작하지 않았다.
    
    # 그 원인을 찾아 보았는데, 상속받은 GenericViewSet 을 따라가다 보면 결국 APIView가
    # 나타난다. 따라서 여기서 정의한 create method와 partial_update method, 
    # destory method는 각 요청에 맞게 동작한다. 
    
    # 반면 list 에 대해서는 따로 정의하지 않았기 때문에 ListModelMixin을 상속받지 않으면
    # get 요청에 대해 응답할 method가 없게 된다. 따라서 get 요청에 대해서는 "not allowed"가
    # 반환된다.
    
    # 이것으로 create, partial_update 등 직접 구현할 동작들에 대해서는 mixin을 따로 상속받지 않아도
    # 된다는 것을 알게 되었다. 바꿔 말하자면 추가로 구현할 동작이 없는 경우에는 단순히 mixin만 상속받으면
    # 정상적으로 동작한다는 것을 알 수 있다.
    
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
            'brand': request.user.brand,
        }
        
        serializer_data = request.data
        serializer = self.serializer_class(
            data = serializer_data, context=serializer_context
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def partial_update(self, request, pk):
        
        try:
            serializer_instance = self.queryset.get(pk=pk)
        except Size.DoesNotExist:
            raise NotFound('The size do not exist.')
        
        serializer_data = request.data
        serializer = self.serializer_class(
            serializer_instance,
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
        
        subcategory_text = self.request.query_params.get('subcategory', None)
        if subcategory_text is not None:
            queryset = queryset.filter(
                subcategory__subcategory__icontains=subcategory_text
                )
        
        category_text = self.request.query_params.get('category', None)
        if category_text is not None:
            queryset = queryset.filter(
                subcategory__category__category__icontains=category_text
                )
        
        product_color_text = self.request.query_params.get('product_color', None)
        if product_color_text is not None:
            queryset = queryset.filter(
                product_color__icontains=product_color_text
            )
        
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
            'subcategory':request.data['subcategory'],
            'request':request
        }
        serializer_data = request.data
        serializer = self.serializer_class(
            data = serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class Product_ImageViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    
    queryset = Product_Image.objects.all()
    serializer_class = Product_ImageSerializer
    permission_class = [
        IsAuthenticated,
        (IsSystemAdmin|IsSiteAdmin|IsMasterVendor|IsGeneralVendor)
        ]

    def get_queryset(self):
        # subcategory_text = self.request.query_params.get('subcategory', None)
        # if subcategory_text is not None:
        #     queryset = queryset.filter(
        #         subcategory__subcategory__icontains=subcategory_text
        #         )
        # User의 brand 명과 image.product.brand 명을 확인해서 queryset을 구성
        # 만약 둘이 다른 경우 not allowed error 발생하도록 설정
        queryset = self.queryset
        
        if self.request.user.brand == 'Admin':
            queryset = self.queryset
        else:
            # product 개별 image list 조회
            product = self.request.query_params.get('product', None)
            if product is not None:
                queryset = queryset.filter(
                    product__pk__contains=product
                )
            else:
                # 해당 brand product의 모든 image list 조회
                queryset = self.queryset.filter(product__brand=self.request.user.brand)
        
        return queryset
    
    
