from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import action
from coastapi.models import Player,Bait,TackleBox
from .bait import BaitSerializer


class TackleBoxSerializer(serializers.ModelSerializer):

    bait = BaitSerializer(many=False)
    class Meta:
        model = TackleBox
        fields = ('id', 'quantity', 'bait')

class Shop(ViewSet):

    @action(methods=['post'], detail=False)
    def purchase_bait(self, request):

        if request.method == 'POST':

            
            player = Player.objects.get(user=request.auth.user)
            bait = Bait.objects.get(pk=request.data["bait"])
            
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
