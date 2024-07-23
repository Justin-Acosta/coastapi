from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .bait import BaitSerializer
from coastapi.models import Population,Player,Fish,Location
from .fish import FishSerializer

class PopulationSerializer(serializers.ModelSerializer):

    fish = FishSerializer(many=False)
    class Meta:
        model = Population
        fields = ('id', 'fish', 'quantity')

class PopulationViewSet(ViewSet):

    def list(self,request,pk=None):

        location = Location.objects.get(pk=request.data["location"])
        population = Population.objects.filter(location=location)

        json_population = PopulationSerializer(population,many=True)

        return Response(json_population.data, status=status.HTTP_200_OK)