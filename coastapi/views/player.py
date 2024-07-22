from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from coastapi.models import Player,Location,TackleBox
from .bait import BaitSerializer
from .shop import TackleBoxSerializer


class PlayerSerializer(serializers.ModelSerializer):

    # player_tacklebox = TackleBoxSerializer(many=True)

    class Meta:
        model = Player
        fields = '__all__'


class Players(ViewSet):

    def retrieve(self,request,pk=None):

        player = Player.objects.get(pk=pk, user=request.auth.user)

        json_player = PlayerSerializer(player,many=False)

        return Response(json_player.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):

        player = Player.objects.get(pk=pk, user=request.auth.user)
        player.nickname = request.data["nickname"]
        player.location = Location.objects.get(pk=request.data["location"])

        player.save()

        json_player = PlayerSerializer(player, many=False, context={'request': request})

        return Response(json_player.data, status=status.HTTP_200_OK)
