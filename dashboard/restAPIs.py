from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *

@api_view(['GET', 'POST'])
def getPendingTransfersCount(request):

    if request.method == 'GET':
        transfers = Transfer.objects.filter(status=True)
        resp = {}
        resp['Pending Transfer Count'] = len(transfers)
        return Response(resp)

    elif request.method == 'POST':
        pass
        # print(type(request.data))
        # serializer = PlantConditionsSerializer(data=request.data)
        # if serializer.is_valid():
        #     # print(serializer.validated_data)
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
