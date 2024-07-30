from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from coastapi.models import FishType,Player

class FishTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FishType
        fields = '__all__'

class FishTypeViewSet(ViewSet):

    def list(self,request,pk=None):

        player = Player.objects.get(user=request.auth.user)
        fish_types = FishType.objects.all()

        json_fish_types = FishTypeSerializer(fish_types,many=True)

        return Response(json_fish_types.data, status=status.HTTP_200_OK)