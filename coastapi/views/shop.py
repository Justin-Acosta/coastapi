from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import action
from coastapi.models import Player,Bait,TackleBox,Fish,PlayerInventory
from .tacklebox import TackleBoxSerializer
from .playerinventory import PlayerInventorySerializer 

class ShopViewSet(ViewSet):

    @action(methods=['post'], detail=False)
    def purchase_bait(self, request):

        if request.method == 'POST':
            
            player = Player.objects.get(user=request.auth.user)
            bait = Bait.objects.get(pk=request.data["bait"])
            
            if bait.price <= player.wallet:
                tacklebox, created = TackleBox.objects.get_or_create(
                    player=player,
                    bait=bait,
                    defaults={'quantity': 1}
                )

                if not created:
                    tacklebox.quantity += 1
                    tacklebox.save()

                player.wallet -= bait.price

                player.save()

                tacklebox = TackleBox.objects.filter(player=player)
                json_tacklebox = TackleBoxSerializer(tacklebox,many=True)


                return Response(json_tacklebox.data, status=status.HTTP_201_CREATED)
            
            return Response({'purchase_successful': False}, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['post'], detail=False)
    def sell_fish(self, request):

        if request.method == 'POST':
   
            player = Player.objects.get(user=request.auth.user)
            fish = Fish.objects.get(pk=request.data["fish"])

            try:
                player_inventory = PlayerInventory.objects.get(player=player,fish=fish)
                
            except PlayerInventory.DoesNotExist:
                return Response({'sale_successful':False},status=status.HTTP_400_BAD_REQUEST)
            
            
            player_inventory.quantity -= 1

            if player_inventory.quantity == 0:
                player_inventory.delete()
            else:
                player_inventory.save()

            player.wallet += fish.price
            player.slots += fish.slots

            player.save()

            player_inventory = PlayerInventory.objects.filter(player=player)
            json_player_inventory = PlayerInventorySerializer(player_inventory,many=True)

            return Response(json_player_inventory.data, status=status.HTTP_201_CREATED)

            
