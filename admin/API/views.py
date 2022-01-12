from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, viewsets

from .serializers import AdminBrandSerializer, AdminUserSerializer, NestedAdminUserSerializer
from .renderers import AdminUserJSONRenderer, AdminBrandJSONRenderer
from authentication.models import User
from brand.models import Brand
from core.permissions import IsSystemAdmin, IsSiteAdmin


class NestedSrializerMixin(viewsets.ModelViewSet):
    read_serializer_class = None
    
    def get_serializer_class(self):
        if self.request.method.lower() =="get":
            return self.read_serializer_class
        return self.serializer_class


# Admin이 User의 정보를 생성, 조회, 수정, 삭제 할 수 있어야 함.
# 따라서 모든 가능을 갖고 있는 ModelViewSet으로 설정할 예정입니다.
class AdminUserViewSet(NestedSrializerMixin):
    
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = (
        IsAuthenticated,
        (IsSystemAdmin|IsSiteAdmin),
    )
    renderer_classes = (AdminUserJSONRenderer,)
    read_serializer_class = NestedAdminUserSerializer
    
    
class AdminBrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = AdminBrandSerializer
    permission_classes = (
        IsAuthenticated,
        (IsSystemAdmin|IsSiteAdmin)
    )
    renderer_classes = (AdminBrandJSONRenderer,)
    

