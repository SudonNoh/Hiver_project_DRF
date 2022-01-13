from rest_framework import status

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

from core.permissions import IsMasterVendor, IsGeneralVendor
from .renderers import BrandJSONRenderer
from .serializers import BrandSerializer
from brand.models import Brand


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
    
    # def patch(self, request, *args, **kwargs):
    #     # serializer instance 보내기
    #     # patch 관련 글 확인하기
        
    #     brand_data = request.data
    #     user_data = request.user.brand
        
    #     serializer_data = {
    #     }
        
    #     serializer = self.serializer_class(
    #         data=serializer_data, partial=True
    #     )

    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
        
    #     return Response(serializer.data, status=status.HTTP_200_OK)