from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from coastapi.models import Player,Location,Bait
from .shop import TackleBoxSerializer


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'

class PlayersViewSet(ViewSet):

    def list(self,request):

        player = Player.objects.get(user=request.auth.user)
        json_player = PlayerSerializer(player,many=False,context={'request':request})

        return Response(json_player.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):

        player = Player.objects.get(pk=pk, user=request.auth.user)
        player.nickname = request.data["nickname"]
        player.location = Location.objects.get(pk=request.data["location"])
        player.wallet = request.data["wallet"]
        if request.data["bait"] is not None:
            player.bait = Bait.objects.get(pk=request.data["bait"])
        else:
            player.bait = None

        player.save()

        json_player = PlayerSerializer(player, many=False, context={'request': request})

        return Response(json_player.data, status=status.HTTP_200_OK)
