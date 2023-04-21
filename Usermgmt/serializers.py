from rest_framework.serializers import ModelSerializer
from .models import User
class UserSerializer(ModelSerializer):
    
    class Meta :
        model = User
        exclude = ['is_staff','is_active','is_superuser','date_joined','last_login','password']