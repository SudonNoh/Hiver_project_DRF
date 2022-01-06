from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import AdminUserSerializer
from .renderers import AdminUserJSONRenderer
from authentication.models import User
from core.permissions import IsSystemAdmin, IsSiteAdmin


class AdminUserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = (
        IsAuthenticated,
        (IsSystemAdmin|IsSiteAdmin),
    )
    renderer_classes = (AdminUserJSONRenderer,)