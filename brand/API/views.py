from rest_framework import status

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

from core.permissions import IsMasterVendor, IsGeneralVendor
from .renderers import BrandJSONRenderer
from .serializers import BrandSerializer
from brand.models import Brand


# Brand를 Create하는 부분은 Site_Admin 영역에서 진행
# Vendor들은 각자 Brand의 정보만을 확인하고, 수정해야하므로
# user의 brand 기준으로 보여주도록 함.
class BrandRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (
        IsAuthenticated, 
        (IsMasterVendor|IsGeneralVendor),
        )
    renderer_classes = (BrandJSONRenderer,)
    serializer_class = BrandSerializer
    
    def get(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(request.user.brand)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        
        request_data = request.data
        user_data = request.user

        serializer_data = {
            'brand_address': request_data.get('brand_address', user_data.brand.brand_address),
            'brand_email': request_data.get('brand_email', user_data.brand.brand_email),
            'brand_homepage': request_data.get('brand_homepage', user_data.brand.brand_homepage),
            'brand_description': request_data.get('brand_description', user_data.brand.brand_description),
            'brand_logo': request_data.get('brand_logo', user_data.brand.brand_logo)
        }
        
        serializer = self.serializer_class(
            user_data.brand, data=serializer_data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)