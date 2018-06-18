from rest_framework.serializers import ModelSerializer
from container.models import Container


class ContainerSerializer(ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'