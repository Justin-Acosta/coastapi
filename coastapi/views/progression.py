from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status


class Progressions(ViewSet):

    @action(methods=['post'], detail=True)
    def progression_state_2(self, request):

        if request.method == 'POST':
            pass
