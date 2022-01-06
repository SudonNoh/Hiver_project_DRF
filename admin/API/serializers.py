from rest_framework import serializers

from authentication.models import User

# Admin이 User의 정보를 생성, 조회, 수정, 삭제 할 수 있어야 함.
# 따라서 모든 가능을 갖고 있는 ModelViewSet으로 설정할 예정
class AdminUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone_number',
            'groups',
            'brand',
            'last_login',
            'is_active',
        ]