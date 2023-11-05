from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from fruit.models import Fruit
from fruit.api.serializers import FruitSerializer


@api_view(["GET", "POST"])
def fruit_list_create_api_view(request):
    if request.method == "GET":
        fruits = Fruit.objects.filter(stock=True)
        serializer = FruitSerializer(fruits, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
