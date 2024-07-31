from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from coastapi.models import ShopInventory,Player
from .bait import BaitSerializer

class ShopInventorySerializer(serializers.ModelSerializer):

    bait = BaitSerializer(many=False)
    class Meta:
        model = ShopInventory
        fields = ('id', 'bait')

class ShopInventoryViewSet(ViewSet):

    def list(self,request,pk=None):

        player = Player.objects.get(user=request.auth.user)
        shop_inventory = ShopInventory.objects.all()

        json_shop_inventory = ShopInventorySerializer(shop_inventory,many=True)

        return Response(json_shop_inventory.data, status=status.HTTP_200_OK)