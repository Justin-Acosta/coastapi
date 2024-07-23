from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import action
import math
import random
from coastapi.models import Location,Player,Population,Bait,TackleBox,Fish,PlayerInventory
from .fish import FishSerializer
from .playerinventory import PlayerInventorySerializer

class LocationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class LocationsViewSet(ViewSet):

    def list(self,request,pk=None):

        player = Player.objects.get(user=request.auth.user)
        locations = Location.objects.all()

        json_locations = LocationsSerializer(locations,many=True)

        return Response(json_locations.data, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=False)
    def catch_fish(self, request):

        if request.method == 'GET':

            player = Player.objects.get(user=request.auth.user)
            location = Location.objects.get(pk=request.data["location"])
            bait = Bait.objects.get(pk=request.data["bait"])
            population = Population.objects.filter(location=location)
            random_weights = []

            try:
                tackle_box = TackleBox.objects.get(player=player,bait=bait)
                
            except TackleBox.DoesNotExist:
                return Response({'bait_available': False},status=status.HTTP_400_BAD_REQUEST)
            
            
            tackle_box.quantity -= 1

            if tackle_box.quantity <= 0:
                tackle_box.delete()
            else:
                tackle_box.save()

            for fish_species in population:

                if fish_species.fish.fish_type.name == "red":
                    fish_species.quantity *= bait.red_modifier + 1
                    fish_species.quantity = math.ceil(fish_species.quantity)
                    random_weights.append(fish_species.quantity)

                if fish_species.fish.fish_type.name == "blue":
                    fish_species.quantity *= bait.blue_modifier + 1
                    fish_species.quantity = math.ceil(fish_species.quantity)
                    random_weights.append(fish_species.quantity)


                if fish_species.fish.fish_type.name == "green":
                    fish_species.quantity *= bait.green_modifier + 1
                    fish_species.quantity = math.ceil(fish_species.quantity)
                    random_weights.append(fish_species.quantity)

                if fish_species.fish.fish_type.name == "yellow":
                    fish_species.quantity *= bait.yellow_modifier + 1
                    fish_species.quantity = math.ceil(fish_species.quantity)
                    random_weights.append(fish_species.quantity)

            caught_fish = random.choices(population,weights=random_weights,k=1)[0]

            json_fish = FishSerializer(caught_fish.fish, many=False)

            return Response(json_fish.data, status=status.HTTP_200_OK)
        
    @action(methods=['post'], detail=False)
    def keep_fish(self, request):

        if request.method == 'POST':

            player = Player.objects.get(user=request.auth.user)
            fish = Fish.objects.get(pk=request.data["fish"])

            if player.slots - fish.slots >= 0:
                player_inventory, created = PlayerInventory.objects.get_or_create(
                    player=player,
                    fish=fish,
                    defaults={'quantity': 1}
                )

                if not created:
                    player_inventory.quantity += 1
                    player_inventory.save()

                player.slots -= fish.slots

                player.save()

                player_inventory = PlayerInventory.objects.filter(player=player)
                json_player_inventory = PlayerInventorySerializer(player_inventory,many=True)

                return Response(json_player_inventory.data, status=status.HTTP_201_CREATED)
            
            return Response({'sufficient_space':False}, status=status.HTTP_400_BAD_REQUEST)
