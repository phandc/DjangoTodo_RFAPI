from rest_framework.serializers import ModelSerializer
from .models import Todo

class TodoSerialier(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title','desc','is_complete']