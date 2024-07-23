from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .bait import BaitSerializer
from coastapi.models import TackleBox,Player

class TackleBoxSerializer(serializers.ModelSerializer):

    bait = BaitSerializer(many=False)
    class Meta:
        model = TackleBox
        fields = ('id', 'quantity', 'bait')

class TackleBoxViewSet(ViewSet):

    def list(self,request,pk=None):

        player = Player.objects.get(user=request.auth.user)
        tackle_box = TackleBox.objects.filter(player=player)

        json_tacklebox = TackleBoxSerializer(tackle_box,many=True)

        return Response(json_tacklebox.data, status=status.HTTP_200_OK)