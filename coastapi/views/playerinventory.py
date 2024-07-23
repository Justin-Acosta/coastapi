from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from coastapi.models import PlayerInventory,Player
from .fish import FishSerializer

class PlayerInventorySerializer(serializers.ModelSerializer):

    fish = FishSerializer(many=False)
    class Meta:
        model = PlayerInventory
        fields = ('id', 'quantity', 'fish')

class PlayerInventoryViewSet(ViewSet):

    def list(self,request,pk=None):

        player = Player.objects.get(user=request.auth.user)
        player_inventory = PlayerInventory.objects.filter(player=player)

        json_player_inventory = PlayerInventorySerializer(player_inventory,many=True)

        return Response(json_player_inventory.data, status=status.HTTP_200_OK)