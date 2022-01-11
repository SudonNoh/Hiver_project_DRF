from rest_framework import status

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer

from core.permissions import IsMasterVendor, IsGeneralVendor
from .renderers import BrandJSONRenderer
from .serializers import BrandSerializer


class BrandRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (
        IsAuthenticated, 
        IsMasterVendor, 
        IsGeneralVendor,
        )
    renderer_classes = (BrandJSONRenderer,)
    Serializer_class = BrandSerializer
    
    def get(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(request.user.brand)
        
        return Response(serializer.data, status=status.HTTP_200_OK)